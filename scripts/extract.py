from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("E-commerce Data Extraction") \
    .getOrCreate()

# Load the dataset
# df = spark.read.csv("..data/ecommerce_data.csv", header=True, inferSchema=True)
df = spark.read.csv("../data/ecommerce_data.csv", header=True, inferSchema=True)

# Count the number of rows
num_rows = df.count()

# Print the number of rows
print(f'The number of rows in the CSV file is: {num_rows}')

# Show the first 5 rows
print("Sample Data:")
df.show(5)

# Print the schema
print("Schema:")
df.printSchema()

# Stop the Spark session
spark.stop()