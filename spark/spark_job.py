

import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum
import time

spark = (
    SparkSession.builder
    .appName("CustomerOrderRevenue")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")

customers = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("/opt/spark/jobs/customers.csv")
)

orders = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("/opt/spark/jobs/orders.csv")
)

# Keep customers where age >= 18
customers_clean = customers.filter(col("age") >= 18)

# Keep completed orders and quantity >= 2
orders_clean = (
    orders
    .filter(col("status") == "Completed")
    .filter(col("quantity") >= 2)
)

# Join orders with valid customers
joined = orders_clean.join(
    customers_clean,
    on="customer_id",
    how="inner"
)

# Calculate total revenue by country and sort descending
result = (
    joined
    .withColumn("revenue", col("quantity") * col("price"))
    .groupBy("country")
    .agg(spark_sum("revenue").alias("total_revenue"))
    .orderBy(col("total_revenue").desc())
)

print("\n===== FINAL REVENUE BY COUNTRY =====")
result.show(truncate=False)

# Force complete execution
result.count()

# Keep the application alive briefly so metrics can be scraped
time.sleep(20000)

spark.stop()
