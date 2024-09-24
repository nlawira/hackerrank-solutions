SELECT
    max(months * salary), count(*)
FROM
    Employee
WHERE
    months * salary = (SELECT max(months * salary) FROM Employee);