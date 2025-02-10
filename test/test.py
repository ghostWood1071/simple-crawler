import json
def read_json(path):
    with open(path, mode="r", encoding="utf-8") as f:
        return json.loads(f.read(), )['data'] 
    
print(read_json("test/result1.json"))