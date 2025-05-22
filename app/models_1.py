from pydantic import BaseModel
from typing import List, Optional

class UserInput(BaseModel):
    message: str
    user_id: Optional[str] = None

class ChatResponse(BaseModel):
    message: str
    severity: str
    suggested_resources: List[str]
