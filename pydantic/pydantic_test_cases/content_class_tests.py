from utility.test_cases_functions.content_class_tests import *

try:
    test_invalid_file_name("_____")
except ValidationError as e:
    print(e)