# ETL Pipeline
# Extract: Sensors / CSV / SQL -> Transform: Cleaning + Feature Eng -> Load: Snowflake / BigQuery
# Spark: df = spark.read.csv('clean_data.csv'); df.groupBy('Type').avg('U').show()
# Hadoop: HDFS storage for 10TB sensor data