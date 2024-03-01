# Assignment-3

Table Structure

The summary table `(summary)` is designed to aggregate information about articles from the refresher_readings table. The schema includes the following columns:

```
TITLE: Title of the article.
TOPIC: Topic of the article.
PUBLISHED_YEAR: Published year of the article. Accepts values from 2018 to 2024.
LEVEL: Level of the article.
LEARNING_OUTCOMES: Learning outcomes of the article.
LINK: Redirect link of the article.
```

Model Definition

The model `(summary.sql)` aggregates data from the raw.refresher_readings.readings table and calculates various statistics such as the number of articles, minimum and maximum lengths of the summary and learning outcomes, for each combination of level, topic, and published year.


Schema Tests

The schema definition `(schema.yml)` includes tests to ensure data quality and integrity:

`not_null`: Ensures that columns do not contain any null values.
`unique`: Checks that each value in the TITLE column is unique.
`accepted_values`: Verifies that the PUBLISHED_YEAR column values are within the accepted range.


Documentation

The schema.yml file includes comments documenting the purpose of each column, providing clarity on the structure and constraints of the schema.

Usage

To use the summary table and associated model and schema tests, follow these steps:


Set up your DBT project and configure it to connect to your Snowflake instance.

Create the model file (summary.sql) in the models directory of your DBT project, containing the SQL logic to aggregate data and calculate statistics.

Define the schema tests in the schema.yml file to ensure data quality and integrity.

Run DBT to execute the model and tests, generating the summary table in your target schema.
