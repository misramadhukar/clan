class Memory:
    def __init__(self):
        self.data = []
    def add(self, item):
        self.data.append(item)
    def get_all(self):
        return self.data

class Tool:
    def __init__(self, name):
        self.name = name
    def run(self, input_data):
        raise NotImplementedError

class BaseAgent:
    def __init__(self, role, tools=None, memory=None, config=None):
        self.role = role
        self.tools = tools or []
        self.memory = memory or Memory()
        self.config = config or {}
    def use_tool(self, tool_name, input_data):
        for tool in self.tools:
            if tool.name == tool_name:
                return tool.run(input_data)
        raise ValueError(f"Tool {tool_name} not found")
    def remember(self, item):
        self.memory.add(item)
    def recall(self):
        return self.memory.get_all()
    def act(self, task, context=None):
        raise NotImplementedError 