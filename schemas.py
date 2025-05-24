from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

#Base
class URLBase(BaseModel):
    short_url: str = Field(..., min_length=6, max_length=10, alias="shortUrl")
    long_url: str = Field(..., min_length=1, max_length=2000, alias="longUrl")
    created_at: datetime | None = None

    model_config = ConfigDict(
        from_attributes = True
    )

#Create
class URLCreate(URLBase):
    pass

#Update
class URLUpdate(URLBase):
    pass

#Response
class URLResponse(URLBase):
    id: int

    model_config = ConfigDict(
        from_attributes = True
    )