from pydantic_models.pydantic_classes import *
import pytest
from pydantic import ValidationError

@pytest.mark.parametrize("invalid_text", "")
def test_invalid_text(invalid_text):
    data = {
        "text": invalid_text,
        "section_title": "Introduction",
        "file_path": "/Users/sudarshan/Big_Data/data.json",
        "para":"0",
        "pages":"('1', '1')"
        
    }
    # Ensure validation error is raised for invalid link
    with pytest.raises(ValidationError) as excinfo:
        MetaDataPDFClass(**data)
    print(str(excinfo.value))

def test_valid_meta_data():
    # Valid data
    data = {
        "text": "Some text from PDF",
        "section_title": "Introduction",
        "file_path": "/Users/sudarshan/Big_Data/data.json",
        "para":"0",
        "pages":"('1', '1')"
        
    }
    # Ensure no validation error is raised
    assert MetaDataPDFClass(**data)


@pytest.mark.parametrize("file_path", "/path/to/nonexistent/file.pdf")
def test_invalid_file_path(file_path):
    # Invalid file path (file does not exist)
    data = {
        "text": "Some text from PDF",
        "section_title": "Introduction",
        "file_path": file_path,
        "para":"0",
        "pages":"('1', '1')"
    }
     # Ensure validation error is raised for invalid link
    with pytest.raises(ValidationError) as excinfo:
        MetaDataPDFClass(**data)
    print(str(excinfo.value))
