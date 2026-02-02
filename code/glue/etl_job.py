"""

AWS Glue Visual ETL Job

Source  : S3 (raw transactions from Kinesis)

Target  : S3 (processed parquet data)

Purpose : Clean, transform, and prepare data for Athena & Redshift

"""

import sys

from pyspark.context import SparkContext

from awsglue.context import GlueContext

from awsglue.job import Job

from awsglue.utils import getResolvedOptions

from pyspark.sql.functions import col, when, current_timestamp

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()

glueContext = GlueContext(sc)

spark = glueContext.spark_session

job = Job(glueContext)

job.init(args['JOB_NAME'], args)

# Visual ETL equivalent: S3 Source

raw_df = spark.read.json("s3://<raw-bucket>/transactions/")

# Visual ETL Transform nodes

transformed_df = (

    raw_df

    .withColumn("amount", col("amount").cast("double"))

    .withColumn("fraud_flag", when(col("amount") > 100000, 1).otherwise(0))

    .withColumn("processed_at", current_timestamp())

)

# Visual ETL target: S3 Sink (Parquet)

transformed_df.write \

    .mode("overwrite") \

    .parquet("s3://<processed-bucket>/processed/")

job.commit()
 
