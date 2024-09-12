SELECT
    CONCAT(Name,'(',LEFT(OCCUPATION,1),')')
FROM
    OCCUPATIONS
ORDER BY
    Name ASC

SELECT 
    CONCAT('There are a total of ' ,count(occupation), ' ', lower(occupation), 's.') AS 'Occupation Count'
FROM
    OCCUPATIONS
GROUP BY
    Occupation
ORDER BY
    [Occupation Count] ASC;