from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

# Initialize Spark session
spark = SparkSession.builder \
    .appName("E-commerce Data Transformation") \
    .getOrCreate()

# Load the dataset
df = spark.read.csv("../data/ecommerce_data.csv", header=True, inferSchema=True)


# Data Cleaning and Transformation
# 1. Handle missing values
df_cleaned = df.na.fill({
    "CustAccountBalance": 0,  # Fill missing account balances with 0
    "CustGender": "Unknown",  # Fill missing genders with "Unknown"
    "brand": "Unknown"        # Fill missing brands with "Unknown"
})

# 2. Remove duplicates
df_cleaned = df_cleaned.dropDuplicates()

# 3. Filter rows where price > 0
df_cleaned = df_cleaned.filter(col("price") > 0)

# 4. Add a new column for transaction type based on price
df_cleaned = df_cleaned.withColumn(
    "transaction_type",
    when(col("price") > 10000, "High Value")
      .when((col("price") > 1000) & (col("price") <= 10000), "Medium Value")
      .otherwise("Low Value")
)

# Show the transformed data
print("Transformed Data:")
df_cleaned.show(5)

# Save the transformed data to a Parquet file
df_cleaned.write.parquet("data/transformed_ecommerce_data.parquet", mode="overwrite")

# Stop the Spark session
spark.stop()