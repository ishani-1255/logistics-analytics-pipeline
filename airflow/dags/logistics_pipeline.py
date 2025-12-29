from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
import pandas as pd

RAW = "/opt/airflow/data/raw/shipments.csv"
PARQUET = "/opt/airflow/data/parquet/shipments.parquet"

def csv_to_parquet():
    df = pd.read_csv(RAW)
    df.to_parquet(PARQUET, index=False)

with DAG(
    "logistics_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    convert = PythonOperator(
        task_id="csv_to_parquet",
        python_callable=csv_to_parquet
    )

    run_dbt = BashOperator(
        task_id="run_dbt",
        bash_command="cd /opt/airflow/dbt/logistics_analytics && dbt run"
    )

    convert >> run_dbt
