from util import data_util
import os

class FileSink():
    def __init__(self, data, **kwargs):
        self.kwargs = kwargs
        self.data = data

    def execute(self):
        file_name = self.kwargs.get("file_name")
        write_mode = self.kwargs.get("write_mode")
        if self.kwargs.get("pattern"):
            pattern_val = data_util.format_pattern(self.kwargs.get("pattern_val"))
            file_name = file_name.replace(self.kwargs.get("pattern"), pattern_val)
        self.data = data_util.convert_data(self.data)
        folder_path = os.path.dirname(file_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path, exist_ok=True)
        with open(f"{file_name}", mode=write_mode) as f:
            f.write(self.data)