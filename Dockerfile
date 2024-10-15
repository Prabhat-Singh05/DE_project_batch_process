FROM apache/airflow:slim-latest-python3.9

# Use the root user to ensure we have permission to install packages
USER root

# Update package lists and install required packages
RUN apt-get update && apt-get install -y \
    awscli \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Switch back to the airflow user (if needed)
USER airflow

# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install --upgrade kafka-python





