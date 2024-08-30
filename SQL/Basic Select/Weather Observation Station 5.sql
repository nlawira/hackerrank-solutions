SELECT
    City,
    length(City)
FROM
    STATION
WHERE
    length(City) = (SELECT max(length(city)) FROM Station) OR
    length(City) = (SELECT min(length(city)) FROM Station)
ORDER BY
    length(City) DESC,
    City ASC
LIMIT 2;