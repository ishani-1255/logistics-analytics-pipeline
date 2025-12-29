FROM apache/airflow:2.7.2

USER airflow

RUN pip install --no-cache-dir \
    duckdb==0.8.1 \
    dbt-core==1.7.18 \
    dbt-duckdb==1.7.5
