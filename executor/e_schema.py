from pydantic import BaseModel


class TakeRsult(BaseModel):
    task_id: int
    task_description: str
    output: str


class ExecutionResult(BaseModel):
    results: list[TakeRsult]
