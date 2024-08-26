SELECT DISTINCT
    City
FROM
    Station
WHERE
    mod(ID,2)=0;