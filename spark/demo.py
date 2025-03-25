# from pyspark.sql import SparkSession

# spark = SparkSession.builder.appName("demo").getOrCreate()

# df = spark.read.parquet("s3a://spark-job-source-datasets/random_user_profile/")

# df.show()


from pyspark.sql import SparkSession
from pyspark.sql.functions import count, sum

# Create a SparkSession
spark = SparkSession.builder.appName("AggregationExample").getOrCreate()

# Sample Data
data = [("Alice", "A", 10), ("Bob", "B", 20), ("Alice", "A", 15), ("Charlie", "B", 25)]
df = spark.createDataFrame(data, ["Name", "Category", "Value"])

# Show the original table
print("Original Data:")
df.show()

# Group by "Category" and calculate aggregations
print("\nAggregated Results:")
aggregated_df = df.groupBy("Category").agg(
    sum("Value").alias("TotalValue"),
    count("*").alias("TotalCount")
)

# Show the aggregated data
aggregated_df.show()

# Send to s3
df.write.format("parquet").mode("overwrite").save("s3://spark-job-data-output/output.parquet")
