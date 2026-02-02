# Real-Time Fraud Detection on AWS (Team Project)

**Authors:** Shubham Kumar & Shruti Katait  
**Stack:** Python, Amazon Kinesis, AWS Lambda, Amazon S3, AWS Glue, Amazon Athena / Amazon Redshift, Amazon QuickSight

## 🚀 Overview
An end-to-end, real-time fraud detection pipeline:
1) Ingest streaming transactions via **Amazon Kinesis**
2) Process & flag suspicious events in **AWS Lambda**
3) Land curated data in an **S3 Data Lake**
4) Detect schema & transform with **AWS Glue**
5) Query with **Amazon Athena** (primary) or **Amazon Redshift** (optional)
6) Visualize trends in **Amazon QuickSight**

## 🛠️ Quick Start
### Prerequisites
- AWS account, CLI configured
- Python 3.10+
- Permissions to create Kinesis, S3, Lambda, Glue, Athena/Redshift, QuickSight

### Steps
1. **Create resources** (Kinesis stream, S3 buckets, IAM roles) via console or IaC of your choice.
2. **Run generator**  
   ```bash
   cd generator
   cp config.example.yaml config.yaml  # update stream name/region
   python3 transaction_generator.py
