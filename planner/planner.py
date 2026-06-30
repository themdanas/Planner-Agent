from planner.prompts import PLANNER_PROMPT
from planner.schemas import PLan
from planner.parser import parse_json


class Planner:
    def __init__(self, client, model):
        self.client = client
        self.model = model

    def build_prompt(self, goal: str):
        return PLANNER_PROMPT.format(goal=goal)

    def create_plan(self, goal:str):
        prompt = self.build_prompt(goal)

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )

        content = response.choices[0].message.content
        plan_dict = parse_json(content)
        plan = PLan.model_validate(plan_dict)

        return plan