SELECT 
    level,
    topic,
    published_year,
    COUNT(title) AS number_of_articles,
    MIN(LENGTH(summary)) AS min_summary_length,
    MAX(LENGTH(summary)) AS max_summary_length,
    MIN(LENGTH(learning_outcomes)) AS min_learning_outcomes_length,
    MAX(LENGTH(learning_outcomes)) AS max_learning_outcomes_length
FROM {{ source('refresher_readings', 'readings') }}
GROUP BY level, topic, published_year