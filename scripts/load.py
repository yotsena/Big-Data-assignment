import os
import duckdb
import pandas as pd
from pyspark.sql import SparkSession

# Ensure the 'data' directory exists
os.makedirs("data", exist_ok=True)

# Initialize Spark session
spark = SparkSession.builder \
    .appName("E-commerce Data Loading") \
    .getOrCreate()

# Load the transformed data from the Parquet file
df_transformed = spark.read.parquet("data/transformed_ecommerce_data.parquet")

# Show the transformed data
print("Transformed Data to be Loaded:")
df_transformed.show(5)

# Convert Spark DataFrame to Pandas DataFrame (for DuckDB compatibility)
df_pandas = df_transformed.toPandas()

import os
print("Current Working Directory:", os.getcwd())
print("Database Exists:", os.path.exists("../data/ecommerce.db"))


# Connect to DuckDB
conn = duckdb.connect("../data/ecommerce.db")  # Make sure the path matches your terminal

# Convert Spark DataFrame to Pandas DataFrame (for DuckDB compatibility)
df_pandas = df_transformed.toPandas()

# Ensure ecommerce_data table is created correctly
conn.execute("CREATE TABLE IF NOT EXISTS ecommerce_data AS SELECT * FROM df_pandas")

# Check if data was inserted
print("Data inserted into ecommerce_data table:")
print(conn.execute("SELECT COUNT(*) FROM ecommerce_data").fetchall())
# Stop Spark session
spark.stop()
