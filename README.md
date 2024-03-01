# Assignment-3

## Problem Statement
Data scraped from web is not validated and cannot be relied.

## Project Goals
Objective is to develop Python classes for validating and processing data from CFA webpage URLs and Grobid PDF outputs, followed by integration with DBT for transformation workflows in Snowflake, while also establishing Test and Production environments for robust deployment.

## Technologies Used
Pydantic
pytest
DBT (Data Build Tool)
    
## Links
Codelab: https://codelabs-preview.appspot.com/?file_id=1bOLtJd9YLoInM7W4p1JACNyj-XZh1Pkn0eEy6gx4R6U/edit?usp=sharing#0


## Project Structure TO BE UPDATED
```
├── README.md
└── pydantic
    ├── Part1.ipynb
    ├── __init__.py
    ├── pydantic_test_cases
    │   ├── __init__.py
    │   ├── content_class_tests.py
    │   ├── metadata_class_tests.py
    │   └── url_class_tests.py
    └── utility
        ├── __init__.py
        ├── pydantic_models
        │   ├── __init__.py
        │   └── pydantic_classes.py
        ├── scraping_with_validation
        │   ├── ReadMe.md
        │   ├── __init__.py
        │   ├── requirements.txt
        │   └── scrapper.py
        └── test_cases_functions
            ├── __init__.py
            ├── content_class_tests.py
            ├── metadata_class_tests.py
            └── url_class_tests.py
```


## How to run Application locally

Execute the files as per step numbers

## References
•	https://docs.getdbt.com/guides/snowflake?step=1Links to an external site.
•	https://courses.getdbt.com/courses/fundamentalsLinks to an external site.
•	https://github.com/Coding-Crashkurse/Pydantic-v2-crashcourseLinks to an external site.

     
## Learning Outcomes
Data Validation: Gain proficiency in implementing data validation using Pydantic, ensuring the integrity and consistency of incoming data.
Data Transformation: Learn how to use DBT for building transformation workflows, enabling the creation of summary tables and other derived data structures.

## Team Information and Contribution 

Name | Contribution %| Contributions |
--- |--- | --- |
Aniket Giram    | 40% |Part 2 |
Sudarshan Dudhe | 40% |Part 1 |
Rasika Kole     | 20% |Part 1, Documentation |
