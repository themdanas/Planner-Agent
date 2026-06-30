from groq import Groq

from planner.planner import Planner

client = Groq()

planner = Planner(
    client=client,
    model="llama-3.3-70b-versatile"
)

goal = "Plan a trip to Japan"

plan = planner.create_plan(goal)

print(plan)