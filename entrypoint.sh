#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

# Initialize the Airflow database
airflow db init

airflow users create \
   --username admin \
   --firstname Admin \
   --lastname User \
   --role Admin \
   --email admin@example.com \
   --password admin_password

# Start the Airflow webserver and scheduler in the background
airflow webserver &
airflow scheduler

# Wait for both processes to finish 
wait
