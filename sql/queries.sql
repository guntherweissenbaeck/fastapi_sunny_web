-- zwischen zwei daten
SELECT *
FROM T_POWER
WHERE (CREATED_AT, CREATED_AT) OVERLAPS (
        '2023-01-01'::DATE,
        '2023-02-01'::DATE
    );

-- kompletter monat
SELECT *
FROM T_POWER
WHERE EXTRACT(
        YEAR
        FROM CREATED_AT
    ) = 2023
    AND EXTRACT(
        MONTH
        FROM CREATED_AT
    ) = 2