FROM apache/superset:3.0.0

USER root

RUN pip uninstall -y duckdb duckdb-engine || true
RUN pip install duckdb==0.8.1 duckdb-engine==0.7.0

USER superset
