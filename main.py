from crawler.playwright_crawler import Crawler
from crawler.request_crawler import RequestCrawler
import json

def read_config(path:str):
    with open(path, mode = "r") as f: 
        config_data = json.loads(f.read())
    return config_data

def run(pipeline_name):
    config = read_config(f"./config/{pipeline_name}")
    crawler = RequestCrawler(config["pipeline"])
    data = crawler.run()
    print(data)
    
    
if __name__ == "__main__":
    run("cafef.json")