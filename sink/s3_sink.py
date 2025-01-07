import boto3
from util import data_util

class S3Sink():
    def __init__(self, data, **kwargs):
        self.data = data
        self.kwargs = kwargs

    def execute(self):
        bucket= self.kwargs.get("bucket")
        file_key = self.kwargs.get("key")  
        self.data = data_util.convert_data(self.data)
        pattern_val = data_util.format_pattern(self.kwargs.get("pattern_val"))
        if self.kwargs.get("pattern"):
            file_key = file_key.replace(self.kwargs.get("pattern"), pattern_val)
        client = boto3.client('s3')
        client.put_object(
            Bucket=bucket,  
            Key=file_key,        
            Body=self.data
        )
