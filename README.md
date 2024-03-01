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
.
├── README.md
├── Step 1
│   ├── ReadMe.md
│   ├── Scraper_cfainstitute-step-1.ipynb
│   ├── requirements.txt
│   └── scrapper.py
├── Step 2
│   ├── 2024-l1-topics-combined-2.pdf
│   ├── 2024-l2-topics-combined-2.pdf
│   ├── 2024-l3-topics-combined-2.pdf
│   ├── Big_Data_Assignment2_step2.ipynb
│   ├── Grobid
│   │   ├── Grobid_RR_2024_l1_combined.txt
│   │   ├── Grobid_RR_2024_l2_combined.txt
│   │   └── Grobid_RR_2024_l3_combined.txt
│   ├── Metadata
│   │   ├── Grobid_RR_2024_l1_combined_metadata.json
│   │   ├── Grobid_RR_2024_l2_combined_metadata.json
│   │   └── Grobid_RR_2024_l3_combined_metadata.json
│   ├── PyPDF
│   │   ├── PyPDF_RR_2024_l1_combined.txt
│   │   ├── PyPDF_RR_2024_l2_combined.txt
│   │   └── PyPDF_RR_2024_l3_combined.txt
│   ├── README.md
│   ├── config.json
│   ├── getting_metadata.py
│   ├── main.py
│   └── requirement.txt
├── Step 3
│   ├── README.md
│   ├── data_upload_to_snowflake__using_sqlalchemy 1.ipynb
│   └── snowflake.py
├── Step 4
│   ├── Big_Data_Assignment2_step4.ipynb
│   ├── CSV
│   │   └── refresher_readings.csv
│   ├── Grobid
│   │   ├── Grobid_RR_2024_l1_combined.txt
│   │   ├── Grobid_RR_2024_l2_combined.txt
│   │   └── Grobid_RR_2024_l3_combined.txt
│   ├── PyPDF
│   │   ├── PyPDF_RR_2024_l1_combined.txt
│   │   ├── PyPDF_RR_2024_l2_combined.txt
│   │   └── PyPDF_RR_2024_l3_combined.txt
│   ├── README.md
│   ├── requirement.txt
│   └── s3_upload.py
├── architecture.py
├── architecture_diagram.png
└── asset
    ├── csv-file-format8052.jpg
    ├── pdf_file.png
    └── txt-file.png
```

*You can generate the project tree using following tools*
*[Project Tree Generator](https://woochanleee.github.io/project-tree-generator)*
*[Generate from terminal](https://www.geeksforgeeks.org/tree-command-unixlinux/)*

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
Sudarshan Dudhe | 30% |Part 1, Part 2 |
Rasika Kole     | 30% |Part 1, Documentation |
