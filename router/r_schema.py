from pydantic import BaseModel, Field

class ToolSelection(BaseModel):
    tool : str