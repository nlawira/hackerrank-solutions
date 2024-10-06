SELECT
    CN.Continent,
    FLOOR(AVG(CT.Population)) AS Pop
FROM
    Country CN
INNER JOIN 
    City CT
ON
    CN.Code = CT.CountryCode
GROUP BY
    CN.Continent
ORDER BY
    Pop ASC;