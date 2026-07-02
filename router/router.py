from planner.parser import parse_json
from router.r_prompt import ROUTER_PROMPT
from router.r_schema import ToolSelection

class Router:
    def __init__(self, client, model, registry):
        self.client = client
        self.model = model
        self.registry = registry

    def build_prompt(self, task: str):
       available_tools = ", ".join(self.registry.list_tools())
       return ROUTER_PROMPT.format(tools=available_tools, task=task)

    def call_llm(self, prompt):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
        )
        return response.choices[0].message.content
    
    def select_tool(self, task: str) -> ToolSelection:
        prompt = self.build_prompt(task)
        output = self.call_llm(prompt)

        output_dict = parse_json(output)

        selection = ToolSelection.model_validate(output_dict)

        return selection