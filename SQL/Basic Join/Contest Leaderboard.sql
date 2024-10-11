SELECT
    ID,
    Name,
    SUM(Max_Score) AS Total_Score
FROM (SELECT
    H.Hacker_id AS ID,
    H.Name AS Name,
    S.Challenge_id AS Challenge,
    MAX(S.Score) AS Max_Score
FROM Hackers H
LEFT JOIN Submissions S
ON H.Hacker_id = S.Hacker_id
GROUP BY ID, Name, Challenge) AS Table1
GROUP BY ID, Name
HAVING
    Total_Score <> 0
ORDER BY
    Total_Score DESC,
    ID ASC;