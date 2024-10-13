SELECT
    S.Name
FROM
    Students AS S
INNER JOIN
    Packages AS P
ON 
    S.ID = P.ID
INNER JOIN
    Friends AS F
ON 
    S.ID = F.ID
INNER JOIN
    Packages AS PF
ON 
    F.Friend_ID = PF.ID
WHERE
    PF.Salary > P.Salary
ORDER BY
    PF.Salary ASC;