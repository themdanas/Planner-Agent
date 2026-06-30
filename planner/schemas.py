from pydantic import BaseModel, Field 

class Task(BaseModel):
    id: int = Field(...,description="Unique task id")
    description: str = Field(...,description="Task description")

class PLan(BaseModel):
    tasks: list[Task]

