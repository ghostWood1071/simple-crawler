from crawler.playwright_crawler import Crawler
from crawler.request_crawler import RequestCrawler
import json
import os
import traceback

def read_config(path:str):
    with open(path, mode = "r") as f: 
        config_data = json.loads(f.read())
    return config_data

def run(pipeline_name):
    config = read_config(pipeline_name)
    crawler = RequestCrawler(config["pipeline"])
    crawler.run()
    
    
if __name__ == "__main__":
    path = "./config/generator/result/"
    # path = "./config/generator/template/"
    # path = "./config/generator/test/"
    files = os.listdir(path)
    for f_index in range(len(files)):
        if files[f_index] == "TIX.json":
            start = f_index
            break
    files = files[start:]
    i = 1
    
    for file in files:
        try:
            run(f"{path}{file}")
        except Exception as e:
            traceback.print_exc()
            print(f"done {i}/{len(files)}")
            i+=1