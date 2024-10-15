{{ 
    config(
        materialized = "table"
)

}}

WITH transform_data_table AS 
(
    SELECT "Date" as "date", 
            "Domain" as domain, 
            "Location" as "location", 
            "Total_Amount" as total_amount,
            "Transaction_count" as transaction_count
    FROM {{ source('raw-data', 'raw_data_table') }} 
    WHERE "Date" IS NOT NULL 
            AND "Total_Amount" IS NOT NULL
            AND "Location" IS NOT NULL 
)


SELECT * FROM transform_data_table

