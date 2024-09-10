SELECT
    CASE
        WHEN ((A = B) AND (B = C)) AND ((A + B > C) AND (A + C > B) AND (B + C > A)) THEN 'Equilateral'
        WHEN ((A = B) OR (B = C) OR (A = C)) AND ((A + B > C) AND (A + C > B) AND (B + C > A)) THEN 'Isosceles'
        WHEN ((A <> B) AND (B <> C)) AND ((A + B > C) AND (A + C > B) AND (B + C > A)) THEN 'Scalene'
        ELSE 'Not A Triangle'
    END AS 'Triangle Type'
FROM
    TRIANGLES;