# Enable DuckDB in Superset
from superset.db_engine_specs.duckdb import DuckDBEngineSpec

DATABASE_ENGINE_SPECS = {
    "duckdb": DuckDBEngineSpec,
}
