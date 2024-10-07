WITH CTE AS (
    SELECT Name, Marks,
        CASE
            WHEN Marks >= 0 and Marks <= 9 THEN 1
            WHEN Marks >= 10 and Marks <= 19 THEN 2
            WHEN Marks >= 20 and Marks <= 29 THEN 3
            WHEN Marks >= 30 and Marks <= 39 THEN 4
            WHEN Marks >= 40 and Marks <= 49 THEN 5
            WHEN Marks >= 50 and Marks <= 59 THEN 6
            WHEN Marks >= 60 and Marks <= 69 THEN 7
            WHEN Marks >= 70 and Marks <= 79 THEN 8
            WHEN Marks >= 80 and Marks <= 89 THEN 9
            ELSE 10
        END AS Grade
    FROM Students
     )

SELECT
    CASE
        WHEN Grade < 8 THEN 'NULL'
        ELSE Name
    End AS Names,
    Grade,
    Marks
FROM
    CTE
ORDER BY
    Grade DESC,
    Names ASC,
    Marks ASC;