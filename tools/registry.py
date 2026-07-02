from tools.base_tool import BaseTool
class ToolRegistry:
    def __init__(self):
        self.tool = {}

    def register(self,tool):
        self.tool[tool.name] = tool

    def get_tool(self, name: str) -> BaseTool | None:
        return self.tool.get(name)

    def list_tools(self):
        return list(self.tool.keys())