from pydantic import BaseModel
from typing import Optional


class Status(BaseModel):
    id: Optional[int] = None
    status_name: Optional[int]

    class Config:
        orm_mode = True
