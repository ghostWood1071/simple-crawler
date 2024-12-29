from crawler import Crawler
import json

def read_config(path:str):
    with open(path, mode = "r") as f: 
        config_data = json.loads(f.read())
    return config_data

def run(pipeline_name):
    config = read_config(f"./config/{pipeline_name}")
    crawler = Crawler(config)
    data = crawler.run()
    print(data)
    
    
if __name__ == "__main__":
    run("vnstock.json")