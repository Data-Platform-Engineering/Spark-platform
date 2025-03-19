from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("demo").getOrCreate()

df = spark.read.parquet("s3a://spark-job-source-datasets/random_user_profile/")

df.show()