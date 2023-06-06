from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: Optional[int] = None
    username: str
    created: Optional[datetime]

    class Config:
        orm_mode = True