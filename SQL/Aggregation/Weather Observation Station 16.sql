SELECT
    round(min(LAT_N),4)
FROM
    Station
WHERE
    LAT_N > 38.7780;