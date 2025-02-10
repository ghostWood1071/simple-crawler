import json
import boto3
from crawler.request_crawler import RequestCrawler
from datetime import datetime, timedelta

def lambda_handler(event, context):
    configs = event["configs"]
    index = event["index"]
    
    if index >= len(configs):
        return {"next_config_available": False}
    date_now = datetime.strptime(datetime.now(), "%d/%m/%Y")
    date_prev = datetime.strptime(datetime.now() - timedelta(days=1), "%d/%m/%Y")
    config = configs[index]
    for step in config["pipline"][0]["actions"]:
        step["params"]["params"]["StartDate"] = date_prev
        step["params"]["params"]["EndDate"] = date_now
    crawler = RequestCrawler(config["pipeline"])
    crawler.run()

    return {
        "configs": configs,
        "index": index + 1, 
        "next_config_available": index + 1 < len(configs)
    }
