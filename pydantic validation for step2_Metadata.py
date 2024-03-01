from pydantic import BaseModel
from pathlib import Path
class MetaDataPDFClass(BaseModel):
    text: str
    section_title: str
    file_path: Path
  

from pydantic import ValidationError
try:
    MetaDataPDFClass(text="_____")
except ValidationError as ex:
    print(ex)

