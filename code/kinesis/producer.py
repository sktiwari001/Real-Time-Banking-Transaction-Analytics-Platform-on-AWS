import json, random, time, boto3
from faker import Faker
 
fake=Faker()
kinesis=boto3.client('kinesis',region_name='us-east-1')
while True:
    txn={"txn_id":fake.uuid4(),
         "account_id":f"ACC{random.randint(1000,9999)}",
         "customer_name": fake.name(),
         "amount":random.randint(100,500000),
         "channel":random.choice(["UPI","ATM","CARD","NETBANKING"]),
         "branch": random.choice(["Delhi","Mumbai","Pune","Bangalore"]),
        "txn_time": fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S")
    }
 
    kinesis.put_record(
        StreamName="banking-transaction-stream",
        Data=json.dumps(txn),
        PartitionKey="banking"
    )
 
    print("Sent:", txn)
    time.sleep(2)
