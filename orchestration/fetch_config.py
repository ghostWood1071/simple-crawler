import boto3
import json

dynamodb = boto3.resource("dynamodb")
table_name = "crawler_job"

def lambda_handler(event, context):
    table = dynamodb.Table(table_name)
    # response = table.scan()
    # configs = response.get("Items", [])
    configs = [table.get_item(Key={"job_id": "9f055e2c-5655-4416-83d6-100ea58cbab8", "name": "AAA"})["Item"]]
    return {
        "configs": configs,
        "index": 0
    }
