WITH article_summary AS (
    SELECT 
        level,
        topic,
        published_year,
        COUNT(title) AS number_of_articles,
        MIN(LENGTH(summary)) AS min_summary_length,
        MAX(LENGTH(summary)) AS max_summary_length,
        MIN(LENGTH(learning_outcomes)) AS min_learning_outcomes_length,
        MAX(LENGTH(learning_outcomes)) AS max_learning_outcomes_length
    FROM raw.refresher_readings.readings
    GROUP BY level, topic, published_year
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