WITH CTE AS (
    SELECT
        H.hacker_id,
        H.name,
        COUNT(S.submission_id) AS "Challenge_Count"
    FROM Hackers H
    INNER JOIN Submissions S
    ON H.hacker_id = S.hacker_id
    INNER JOIN Challenges C
    ON S.challenge_id = C.challenge_id
    INNER JOIN Difficulty D
    ON C.difficulty_level = D.difficulty_level
    WHERE
        S.Score = D.Score
    GROUP BY
        H.hacker_id, H.name
    )

SELECT
    hacker_id,
    name
FROM CTE
WHERE
    Challenge_Count > 1
ORDER BY
    Challenge_Count DESC,
    hacker_id ASC;