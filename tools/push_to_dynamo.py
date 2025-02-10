import boto3
import os
import json

# Kết nối DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('crawler_job')

config_path = "config/generator/result"
tickers = os.listdir(config_path)

i = 1
len_ = len(tickers)
for ticker in tickers:
    with open(f"{config_path}/{ticker}", mode = 'r') as f:
        data = json.loads(f.read())
    table.put_item(Item=data)
    print(f"done {i}/{len_}")
    i += 1

