WITH CTE AS (
    SELECT 
        h.hacker_id AS hacker_id,
        name,
        COUNT(ch.challenge_id) AS chalenges_count,
        COUNT(COUNT(ch.challenge_id)) OVER (PARTITION BY COUNT(ch.challenge_id)) AS same_results
    FROM hackers h
        JOIN challenges ch
        ON h.hacker_id = ch.hacker_id
    GROUP BY h.hacker_id, name
    )

SELECT 
    hacker_id,
    name,
    chalenges_count
FROM CTE    
WHERE same_results = 1 
OR chalenges_count = (SELECT MAX(chalenges_count) FROM CTE)
ORDER BY
    chalenges_count DESC,
    hacker_id;