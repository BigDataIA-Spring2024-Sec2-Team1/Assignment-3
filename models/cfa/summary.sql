{{
  config(
    materialized='view'
  )
}}

WITH article_summary AS (
    select * from {{ ref('article_summary') }}
),

summary as (
    select 
        level as Level,
        topic AS Topic,
        published_year AS P_Year,
        number_of_articles AS Number_of_articles,
        min_summary_length AS Min_Length_Summary,
        max_summary_length AS Max_Length_Summary,
        min_learning_outcomes_length AS Min_Learning_Outcomes,
        max_learning_outcomes_length AS Max_Learning_Outcomes
    from article_summary
)

select * from article_summary