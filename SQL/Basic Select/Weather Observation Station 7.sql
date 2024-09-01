SELECT DISTINCT
    City
FROM
    Station
WHERE
    City LIKE '%a' OR
    City LIKE '%e' OR
    City LIKE '%i' OR
    City LIKE '%o' OR
    City LIKE '%u';