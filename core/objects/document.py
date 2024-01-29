from pydantic import BaseModel
from datetime import datetime


class Document(BaseModel):
    id: str
    index: str
    category: str
    created_at: datetime
    author: str
    content_type: str
    content: str
    reach: int
    shares: int
    replays: int
    interactions: int

