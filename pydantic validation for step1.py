from pydantic import BaseModel, HttpUrl
from typing import Optional
class URLClass(BaseModel):
    title: str
    topic: str
    year: int
    link: HttpUrl
    level: str
    introduction: str
    learning_outcomes: str
    summary: Optional[str]
    

from pydantic import ValidationError
try:
    URLClass(title="_____")
except ValidationError as ex:
    print(ex)

