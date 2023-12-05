from datetime import datetime

from pydantic import BaseModel

from enums import Mark


class ReviewBase(BaseModel):
    text: str
    data: datetime
    rating: Mark
    user_id: int


class ReviewCreation(ReviewBase):
    ...


class ReviewRead(ReviewBase):
    id: int

    class Config:
        from_attributes = True