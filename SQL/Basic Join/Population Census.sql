SELECT
    SUM(C.Population)
FROM
    City AS C
INNER JOIN Country as D
ON C.CountryCode = D.Code
WHERE
    D.Continent = "Asia";