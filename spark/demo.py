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

age = StructField("Age",IntegerType(),True)
attrition = StructField("Attrition",StringType(),True)
business_travel = StructField("BusinessTravel",StringType(),True)
department = StructField("Department",StringType(),True)
Dist_from_home = StructField("DistanceFromHome",IntegerType(),True)
education = StructField("EducationField",StringType(),True)
emp_no = StructField("EmployeeNumber",IntegerType(),True)
env_satisfaction = StructField("EnvironmentSatisfaction",IntegerType(),True)
gender = StructField("Gender",StringType(),True)
hourly_rate = StructField("HourlyRate",IntegerType(),True)
jobinvolvement = StructField("JobInvolvement",IntegerType(),True)
job_level = StructField("JobLevel",IntegerType(),True)
job_role = StructField("JobRole",StringType(),True)
job_satisfaction = StructField("JobSatisfaction",IntegerType(),True)
marital_status = StructField("MaritalStatus",StringType(),True)
monthly_income = StructField("MonthlyIncome",IntegerType(),True)
monthly_rate = StructField("MonthlyRate",IntegerType(),True)
no_of_comp_worked= StructField("NumCompaniesWorked",IntegerType(),True)
over18 = StructField("Over18",StringType(),True)
over_time = StructField("OverTime",StringType(),True)

columnList = [age, attrition, business_travel,department,Dist_from_home,education,emp_no,env_satisfaction,gender,hourly_rate,jobinvolvement,job_level,job_role,job_satisfaction,marital_status,monthly_income,monthly_rate,no_of_comp_worked,over18,over_time]
empDfSchema = StructType(columnList)

# empDf = spark.read.csv('s3://spark-job-source-datasets/emp_dataset.csv', header=True,schema=empDfSchema)
#  empDf = spark.read.csv('/Users/user/Downloads/emp_dataset.csv', header=True,schema=empDfSchema)

empDf = spark.read.csv('s3://spark-data-sources/emp_dataset.csv', header=True,schema=empDfSchema)


empDf.show(4)

groupedOnBusinessTravel = empDf.groupby(["BusinessTravel"]).mean()
groupedOnBusinessTravel.show()

grouponGender = empDf.groupby(["Gender"]).mean()
grouponGender.show(4)

sumOfmonthIncome = empDf.groupby("Gender").sum("MonthlyIncome")
sumOfmonthIncome.show()

# Send to s3
groupedOnBusinessTravel.write.format("parquet").mode("overwrite").save("s3://spark-job-data-output/groupedOnBusinessTravel.parquet")
grouponGender.write.format("parquet").mode("overwrite").save("s3://spark-job-data-output/grouponGender.parquet")
sumOfmonthIncome.write.format("parquet").mode("overwrite").save("s3://spark-job-data-output/sumofMonthIncome.parquet")

# Send to s3
# groupedOnBusinessTravel.write.format("parquet").mode("overwrite").save("s3://spark-job-data-output")
# grouponGender.write.format("parquet").mode("overwrite").save("s3://spark-job-data-output")
# sumOfmonthIncome.write.format("parquet").mode("overwrite").save("s3://spark-job-data-output")


# Send to local
# groupedOnBusinessTravel.write.format("csv").mode("append").save("groupedOnBusinessTravel.csv")
# grouponGender.write.format("csv").mode("overwrite").save("grouponGender.csv")
# sumOfmonthIncome.write.format("csv").mode("overwrite").save("sumOfmonthIncome.csv")
