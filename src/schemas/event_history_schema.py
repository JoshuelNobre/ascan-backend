from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class EventHistory(BaseModel):
    id: Optional[int] = None
    subscription_id: Optional[int]
    type: Optional[int]
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
