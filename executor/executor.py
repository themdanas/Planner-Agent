from unittest import TestResult

from executor.e_prompt import EXECUTOR_PROMPT
from executor.e_schema import ExecutionResult, TakeRsult


class Executor:
    def __init__(self, client, model, router, registry):
        self.client = client
        self.model = model
        self.router = router
        self.registry = registry


    def build_prompt(self, task: str):
        return EXECUTOR_PROMPT.format(task=task)

    def call_llm(self, prompt):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content

    def execute_task(self, task):
        
        selection = self.router.select_tool(task.description) # ask router which tool to use 

        # LLM execution
        if selection.tool.lower() == "llm":
            prompt = self.build_prompt(task.description)
            output = self.call_llm(prompt)
        
        # tools execution
        else:
            tool = self.registry.get_tool(selection.tool)

            if tool is not None:
                output = tool.execute(task.description)
            
            else:
                #fallback to LLM if tool not found
                prompt = self.build_prompt(task.description)
                output = self.call_llm(prompt)

        return TakeRsult(
            task_id=task.id,
            task_description=task.description,
            output=output
        )

    def execute_plan(self, plan):
        results = []
        for task in plan.tasks:
            result = self.execute_task(task)
            results.append(result)

        execution = ExecutionResult(results=results)
        return execution

    