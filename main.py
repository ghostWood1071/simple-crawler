from crawler.playwright_crawler import Crawler
from crawler.request_crawler import RequestCrawler
import json
import os

def read_config(path:str):
    with open(path, mode = "r") as f: 
        config_data = json.loads(f.read())
    return config_data

def run(pipeline_name):
    config = read_config(pipeline_name)
    crawler = RequestCrawler(config["pipeline"])
    crawler.run()
    
    
if __name__ == "__main__":
    # path = "./config/generator/result/"
    path = "./config/generator/template/"
    files = os.listdir(path)
    i = 1
    for file in files:
        try:
            run(f"{path}{file}")
        except Exception as e:
            print(f"done {i}/{len(files)}")
            i+=1