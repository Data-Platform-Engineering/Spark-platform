# # from pyspark.sql import SparkSession

# # spark = SparkSession.builder.appName("demo").getOrCreate()

# # df = spark.read.parquet("s3a://spark-job-source-datasets/random_user_profile/")

# # df.show()


# from pyspark.sql import SparkSession
# from pyspark.sql.functions import count, sum

# # Create a SparkSession
# spark = SparkSession.builder.appName("AggregationExample").getOrCreate()

# # Sample Data
# data = [("Alice", "A", 10), ("Bob", "B", 20), ("Alice", "A", 15), ("Charlie", "B", 25)]
# df = spark.createDataFrame(data, ["Name", "Category", "Value"])

# # Show the original table
# print("Original Data:")
# df.show()

# # Group by "Category" and calculate aggregations
# print("\nAggregated Results:")
# aggregated_df = df.groupBy("Category").agg(
#     sum("Value").alias("TotalValue"),
#     count("*").alias("TotalCount")
# )

# # Show the aggregated data
# aggregated_df.show()

# # Send to s3
# df.write.format("parquet").mode("overwrite").save("s3://spark-job-data-output/output.parquet")

# import pyspark
# from pyspark.sql import SparkSession
# from pyspark.sql.functions import *
# from pyspark.sql.types import *
# spark = SparkSession.builder.appName('Aggregation on Single col').getOrCreate()


import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

# Initialize Spark with proper logging configuration
spark = SparkSession.builder \
    .appName('Aggregation on Single col') \
    .config("spark.driver.extraJavaOptions", "-Dlog4j.configuration=file:/etc/spark/log4j.properties") \
    .getOrCreate()

# Reduce log noise (optional)
spark.sparkContext.setLogLevel("WARN")


df = spark.read.csv('s3://spark-data-sources/emp_dataset.csv', header=True, inferSchema=True)

df.groupBy("BusinessTravel").agg({"Age": "sum"}).sort("BusinessTravel").show()
df = df.groupBy("BusinessTravel").agg({"Age": "sum"}).sort("BusinessTravel")
rename_df = df.withColumnRenamed('sum(Age)', 'total_age')
rename_df.show()
rename_df.write.parquet("s3a://spark-job-data-output/spark_output/employee_ayo/",mode="overwrite")


# empDf = spark.read.csv('s3://spark-data-sources/emp_dataset.csv', header=True, inferSchema=True)
# empDf.show(4)

# business = empDf.groupBy("BusinessTravel").agg({"Age": "sum"}).sort("BusinessTravel").show()


# rename_df = business.withColumnRenamed('sum(Age)', 'total_age')

# grouponBusinessTravel = rename_df #added now
# grouponGender = empDf.groupBy("Gender").agg({"Age": "sum"}).withColumnRenamed('sum(Age)', 'total_age').show() 
# sumOfmonthIncome = empDf.groupBy("Gender").agg({"MonthlyIncome": "sum"}).withColumnRenamed('sum(Age)', 'total_age').show()
