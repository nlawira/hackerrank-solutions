SELECT
    CEIL(AVG(Salary) - AVG(cast(replace(cast(Salary as CHAR), '0','') as UNSIGNED)) ) AS ERROR
FROM
    EMPLOYEES;