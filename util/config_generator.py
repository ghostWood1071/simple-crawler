import json
import pandas as pd
import copy
import re
import uuid

class ConfigGenerator():
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.config = self.read_config(self.config_path)
        self.template = self.read_config(self.config["template"])
        self.gen_data:pd.DataFrame = None
    
    def read_config(self, path):
        with open(path, mode = 'r') as f:
           return json.loads(f.read())
        

    def load_config(self):
        match self.config["format"]:
            case "excel":
                self.gen_data = pd.read_excel(self.config["path"], self.config.get("sheet"))
            case _:
                raise NotImplementedError("format not implemented")
            
    def write_config(self, path, config):
        with open(path, mode = 'w') as f:
            f.write(config)
    
    def get_next_ticker(self, tickers, index):
        if index >= len (tickers):
            return None
        return tickers[index]

    def execute(self):
        mapping = self.config["mapping"]
        tickers = [x[1]['Ticker'] for x in self.gen_data.iterrows()]
        for index, row in self.gen_data.iterrows():
            config = json.dumps(self.template)
            for field in mapping.keys():
               config = config.replace(mapping[field], row[field])
            path_config = re.sub(r"\{(\w+)\}", lambda match: row.to_dict().get(match.group(1), match.group(0)), self.config["output"])
            config = json.loads(config)
            config["next"] = self.get_next_ticker(tickers, index+1)
            config["job_id"] = str(uuid.uuid4())
            config = json.dumps(config)
            self.write_config(path_config, config)
    