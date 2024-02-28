from pydantic import BaseModel
from typing import Union
class ContentPDFClass(BaseModel):
    file_name: str
    extracted_content: Union[int, str]
  

from pydantic import ValidationError
try:
    ContentPDFClass(file_name="_____")
except ValidationError as ex:
    print(ex)

