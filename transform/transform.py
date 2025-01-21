import importlib.util

class Transform:
    def __init__(self, data ,**kwargs):
        self.kwargs = kwargs
        self.data = data

    def process(self):
        spec = importlib.util.spec_from_file_location("dynamic_module", self.kwargs.get("path"))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, "process"):
            func = getattr(module, "process")
            result = func(self.data)
            return result
        
        print(f"Function process not found in the module.")

