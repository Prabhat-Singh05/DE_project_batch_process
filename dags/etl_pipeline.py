from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import boto3
#import os
import pandas as pd
from kafka import KafkaProducer
from sqlalchemy import create_engine
import psycopg2

S3_BUCKET = 'de-batch-process'
S3_KEY = 'raw-data/bankdataset.csv'
KAFKA_TOPIC = 'raw-data'

def download_from_s3():
    """Download raw data from S3."""
    s3 = boto3.client('s3')
    s3.download_file(S3_BUCKET, S3_KEY, '/tmp/raw_data.csv')

def send_to_kafka():
    """Send data to Kafka."""
    producer = KafkaProducer(bootstrap_servers='kafka:9092')
    with open('/tmp/raw_data.csv', 'r') as file:
        for line in file:
            producer.send(KAFKA_TOPIC, value=line.encode('utf-8'))
    producer.close()
    
def load_to_postgres():
    """Load CSV data into PostgreSQL using psycopg2."""
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname='airflow', 
        user='airflow', 
        password='airflow', 
        host='postgres', 
        port='5432'
    )
    
    cursor = conn.cursor()
    
    # Load the CSV data into a pandas DataFrame
    df = pd.read_csv('/tmp/raw_data.csv')
    
    # Create the 'raw_data' table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS raw_data_table (
            "Date" date,
            "Domain" varchar(20),
            "Location" varchar(30),
            "Total_Amount" float,
            "Transaction_count" int
        )
    """)
    
    # Insert data into PostgreSQL row by row
    for index, row in df.iterrows():
        cursor.execute("""
            INSERT INTO raw_data_table ("Date", "Domain", "Location", "Total_Amount", "Transaction_count")
            VALUES (%s, %s, %s, %s, %s)""",
            tuple(row)
        )
    
    # Commit the transaction
    conn.commit()
    
    # Close the connection
    cursor.close()
    conn.close()
    


with DAG('etl_pipeline', 
         start_date=datetime(2024, 10, 10), 
         schedule_interval='@once') as dag:

    download_task = PythonOperator(
        task_id='download_from_s3',
        python_callable=download_from_s3
    )

    kafka_task = PythonOperator(
        task_id='send_to_kafka',
        python_callable=send_to_kafka
    )

    load_postgres_task = PythonOperator(
        task_id='load_to_postgres',
        python_callable=load_to_postgres
    )

    download_task >> kafka_task >> load_postgres_task 
