from tools.base_tool import BaseTool

class Calculator(BaseTool):
    def __init__(self):
        super().__init__(
            name="Calculator",
            description="Performs basic mathematical calculations"
        )

    def execute(self, query: str):
        try:
            result = eval(query)
            return str(result)
        except Exception as e:
            return f"Calculation error: {e}"
