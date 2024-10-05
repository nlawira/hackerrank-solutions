SELECT
    C.Name
FROM
    City C
INNER JOIN Country D
ON C.CountryCode = D.Code
WHERE
    D.Continent = "Africa";