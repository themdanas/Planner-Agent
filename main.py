import os
from groq import Groq
from planner.planner import Planner
from executor.executor import Executor
from tools.registry import ToolRegistry
from tools.calculator import Calculator as CalculatorTool
from router.router import Router


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

model="llama-3.3-70b-versatile"

registry = ToolRegistry()
registry.register(CalculatorTool())

router = Router(
    client=client,
    model=model,
    registry=registry
)

planner = Planner(
    client=client,
    model=model
)

executor=Executor(
    client=client,
    model=model,
    router=router,
    registry=registry
)

#user goal

goal = input("Enter your goal: ")

#plannig

plan = planner.create_plan(goal)
print("\n" + "=" * 60)
print("PLAN")
print("=" * 60)

for task in plan.tasks:
    print(f"{task.id}. {task.description}")

#execution

execution = executor.execute_plan(plan)

print("\n" + "=" * 60)
print("EXECUTION")
print("=" * 60)

for result in execution.results:

    print(f"\nTask {result.task_id}")

    print(f"Description : {result.task_description}")

    print("-" * 50)

    print(result.output)

    print("-" * 50)

