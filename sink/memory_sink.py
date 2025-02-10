class MemorySinhk():
    sink = {}
    def __init__(self, data, **kwargs):
        self.data = data
        self.kwargs = kwargs
    
    def execute(self):
        if self.kwargs.get("value"):
            MemorySinhk.sink[self.kwargs.get("name")] = self.kwargs.get("value")
        else:
            MemorySinhk.sink[self.kwargs.get("name")] = self.data
        return MemorySinhk.sink
    
    def clear(self):
        MemorySinhk.sink = {}