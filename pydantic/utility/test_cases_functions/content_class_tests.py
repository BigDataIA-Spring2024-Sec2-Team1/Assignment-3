from pydantic_models.pydantic_classes import *
import pytest
from pydantic import ValidationError

@pytest.mark.parametrize("file_name", "____")
def test_invalid_file_name(file_name):
    # Invalid file path (file does not exist)
    data = {
        "file_name": file_name,
        "extracted_content": "example extracted content"
    }
     # Ensure validation error is raised for invalid link
    with pytest.raises(ValidationError) as excinfo:
        ContentPDFClass(**data)
    print(str(excinfo.value))
    

