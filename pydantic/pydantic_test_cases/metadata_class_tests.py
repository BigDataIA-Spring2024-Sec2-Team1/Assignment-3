from utility.test_cases_functions.metadata_class_tests import *

try:
    test_valid_meta_data()
except ValidationError as e:
    print(e)
    

try:
    test_invalid_text("")
except ValidationError as e:
    print(e)

try:
    test_invalid_file_path("/path/to/nonexistent/file.pdf")
except ValidationError as e:
    print(e)