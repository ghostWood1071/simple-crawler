import requests
import traceback 
from sink.sink import Sink
import json
import time
from util import data_util
import copy
from error.page_end_error import PageEndError
from transform.transform import Transform

class RequestCrawler():
    def __init__(self, pipeline):
        self.pipeline = pipeline
        self.api_params = ["params", "headers", "data"]

    def call_api(self, input_val ,**kwargs):
        try:
            api_params_dict = {}
            for api_param in self.api_params:
                if kwargs.get(api_param):
                    api_params_dict[api_param] = data_util.format_params(kwargs.get(api_param), kwargs)
                else:
                    api_params_dict[api_param] = None
            method = kwargs.get("method")
            response = getattr(requests, method)(
                kwargs.get("url"), 
                params=api_params_dict["params"], 
                headers=api_params_dict["headers"], 
                data=api_params_dict["data"], 
                cookies=kwargs.get("cookies")
            )
            if kwargs.get("format"):
                result = response.__getattribute__(kwargs.get("format"))()
            else:
                result = response.raw
            if kwargs.get("cond"):
                expr = kwargs["cond"]["validate"]
                if eval(expr):
                    raise PageEndError(f"done")
            return result
        except PageEndError as e:
            raise e
        except Exception as e:
            traceback.print_exc()
    
    def save(self, input_val, **kwargs):
        result = Sink(kwargs.get("type"), input_val, **kwargs).execute()
        return result
    
    def clear_sink(self, input_val, **kwargs):
        Sink(kwargs.get("type"), input_val, **kwargs).clear()
    
    def transform(self, input_val, **kwargs):
        try: 
            return Transform(input_val, **kwargs).process()
        except PageEndError as e:
            raise e

    def foreach(self, input_val, **kwargs):
        iterator = []
        if isinstance(input_val, list):
            iterator = input_val
        if kwargs.get("limit"):
            limit = kwargs.get("limit")
            start = 0
            step = 1
            if kwargs.get("start"):
                start  = kwargs.get("start")
            if kwargs.get("step"):
                step = kwargs.get("step")
            iterator = range(start, limit, step)
            
        for item in iterator:
            actions = copy.deepcopy(kwargs["actions"])
            tmp_val = item
            for action in actions:
                try:
                    params = action["params"]
                    params["item"] = item
                    if isinstance(tmp_val, dict):
                        if action["params"].get("set_prev_result_as_params"):
                            params.update(tmp_val)
                    if kwargs.get("cond"):
                        if kwargs["cond"]["action"] == action.get("name"):
                            params["cond"] = kwargs["cond"]
                    tmp_val = getattr(self,action.get("name"))(tmp_val, **params)
                except PageEndError as e:
                    raise e
                except Exception as e:
                    traceback.print_exc()
            if kwargs.get("delay"):
                time.sleep(kwargs.get("delay"))
        return tmp_val
    
    def run(self):
        tmp_val = None
        for action in self.pipeline:
            method = getattr(self, action.get("name"))
            tmp_val = method(tmp_val, **action.get("params"))
        return tmp_val
    

