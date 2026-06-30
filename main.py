import os
from groq import Groq
from planner.planner import Planner
from executor.executor import Executor

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

model="llama-3.3-70b-versatile"

planner = Planner(
    client=client,
    model=model
)

executor=Executor(
    client=client,
    model=model
)


goal = input("Enter your goal: ")

#planning phase

plan = planner.create_plan(goal)

print("\n" + "=" * 60)
print("PLAN")
print("=" * 60)

for task in plan.tasks:
    print(f"{task.id}.{task.description}")

#execution phase

execution=executor.execute_plan(plan)

print("\n" + "=" * 60)
print("EXECUTION")
print("=" * 60)


for result in execution.results:
    print(f"\nTask {result.task_id}")
    print(f"Description : {result.task_description}")
    print(f"Output :\n{result.output}")