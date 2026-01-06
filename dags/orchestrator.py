import sys
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

sys.path.append('/opt/airflow/src')

from insert_data import main

default_args = {
    'description':'DAG to orchestrate data',
    'start_date':datetime(2026, 6, 1),
    'catchup':False,
}

dag = DAG(
    dag_id='weather-api-orchestrator',
    default_args=default_args,
    schedule=timedelta(minutes=1)
)
with dag:
    task1 = PythonOperator(
        task_id='ingest_data_task',
        python_callable=main
    )