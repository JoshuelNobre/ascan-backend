from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class Subscription(BaseModel):
    id: Optional[int] = None
    user_id: Optional[int]
    status_id: Optional[int]
    created_at: Optional[datetime]
    modified_at: Optional[datetime]

    class Config:
        orm_mode = True

