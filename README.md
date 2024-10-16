# DE Project - Batch Processing Pipeline

## Overview: 
In this project, we design and build a batch-processing data pipeline that takes raw data from a local file, uploads it to AWS S3, processes the data, and then stores it in PostgreSQL after applying transformations using dbt (Data Build Tool). The pipeline leverages popular data engineering tools such as Kafka for real-time streaming, Airflow for orchestration, and Docker for containerizing and managing dependencies.

The key objectives of this project are:

* Data Ingestion: Move raw data from a local source to AWS S3.
* Data Processing: Stream the data from S3 to Kafka and then to PostgreSQL.
* Data Transformation: Use dbt to transform the raw data into a cleaned, organized form within the PostgreSQL database.
* Orchestration: Airflow coordinates and automates the entire pipeline, ensuring smooth transitions between the stages.
* Reproducibility: The entire setup is containerized using Docker, making it easy for others to rerun the pipeline by deploying the Docker containers.


## Introduction:
In today’s data-driven world, building reliable, scalable, and maintainable data pipelines is essential for processing and analyzing large volumes of data efficiently. This project aims to demonstrate the power of a batch-processing architecture by integrating several tools and technologies that are widely used in the industry. The pipeline you will build follows the principles of modern data architecture, ensuring flexibility, fault-tolerance, and reproducibility.

The pipeline is broken into the following components:

- AWS S3: For data storage. The raw data is first uploaded to an S3 bucket.
- Kafka: For streaming data between systems. Once data is available in S3, Kafka producers send the data to a topic that consumers can read from.
- PostgreSQL: As the destination database where the processed and transformed data is stored.
- dbt: For transforming raw data into a structured and analyzed format, applying necessary transformations in the PostgreSQL database.
- Airflow: As the orchestrator, automating the entire workflow from data ingestion to transformation.
- Docker: To ensure that the whole project can be run on any system, regardless of local dependencies or configurations.

## Pipeline Architecture:
![image](https://github.com/user-attachments/assets/92d7feb6-7d59-4eac-8510-9f5bd6b0c010)


## Data Source:
The project's data set was sourced from Kaggle; it is a randomly created Python dataset that
has no connection to any business. There are almost a million records in this dataset.

Source link: https://www.kaggle.com/datasets/ksabishek/massive-bank-dataset-1-million-rows

Note - the data file is converted to csv file format which is kept in data folder. 

## Data Sturcture:
- Date - The date on which the transaction took place.
- Domain - Where or which type of Business entity made the transaction.
- Location - Where the data is collected from.
- Total_Amount - Total value of transaction.
- Transaction_count - total number transaction happend on the particular date.

## Project Setup:
### Clone Repository:

To clone this repository, open terminal, type the following command:
```
git clone https://github.com/Prabhat-Singh05/DE_project_batch_process.git
```

### Prerequisite:
Make sure you have install docker desktop & docker compose in you system.

link - https://www.docker.com/products/docker-desktop/

To check if the intstallation is completed properly
```
docker compose version
```

Also, install Postgres GUI 

### Environment

Create a file .env at the root dirtectly level folder and provide the access key and secret key:
```
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
```
Note: the access key is given in the submission document copy it from there

### For running the code

- Open VScode and open terminal

- In linux/Mac give access to entrypoint.sh file 
```
chmod +x entrypoint.sh
```
- open docker desktop app
- Then again VS code terminal and run the below cmd to build the image:
```
docker build -t my_airflow_image:v1.0 .
```
- check the docker image
```
docker imagaes
```
- To run docker container
```
docker compose up -d
```
- Once the the container is up and running:
  * open your browser to enter http://localhost:8080 to access airflow
  * Username and password is provided in entrypoint.sh file copy from there.

- trigger the dag
- once the dag is completed. Setup Postgres GUI to access the database use --port 5431 && user and password is "airflow"
- Check the raw_data_table is created and all data is populated correctly
- Open a new terminal and use the cmd to create a venv:
```
python -m venv dbt-env				# create the environment
```
- activate the environment for Mac and Linux
```
source dbt-env/bin/activate
```
- Install dbt-core
```
pip install dbt-core
```
- Install dbt-postgres adapter
```
pip install dbt-postgres
```
- change working directry to dbt_transform folder
```
cd ./dbt_transform
```
```
dbt init       #to initialize dbt in the folder
```
- To check connection between dbt and postgre
```
dbt debug
```
- To build table and check data qaulity test
```
dbt build
```
- Once the process is completed. Check in postgres the transform_data_table is created and all data is populated correctly
