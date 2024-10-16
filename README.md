# DE Project Batch Processing

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

![image](https://github.com/user-attachments/assets/92d7feb6-7d59-4eac-8510-9f5bd6b0c010)


