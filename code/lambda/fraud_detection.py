import json
import boto3
import base64
from datetime import datetime
 
s3 = boto3.client('s3')
BUCKET = "banking-datalake-yourname"
 
def lambda_handler(event, context):
    for record in event['Records']:
        payload = base64.b64decode(record['kinesis']['data']).decode("utf-8")
        txn = json.loads(payload)
 
        # Fraud rule
        txn["is_suspicious"] = "YES" if txn["amount"] > 200000 else "NO"
        txn["processed_time"] = str(datetime.now())
 
        file_name = f"raw/transactions/{txn['txn_id']}.json"
 
        s3.put_object(
            Bucket=BUCKET,
            Key=file_name,
            Body=json.dumps(txn)
        )
 
    return {"status": "success"}
 
 
