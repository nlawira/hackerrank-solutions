WITH
vieu AS (
    SELECT COL.contest_id,
           SUM(vs.total_views) AS tv,
           SUM(vs.total_unique_views) AS tuv
    FROM Colleges COL
    JOIN Challenges CHAL
    ON CHAL.college_id = COL.college_id
    JOIN View_Stats vs
    ON vs.challenge_id = CHAL.challenge_id
    GROUP BY COL.contest_id
),
submission AS (
    SELECT COL.contest_id,
           SUM(ss.total_submissions) AS ts,
           SUM(ss.total_accepted_submissions) AS tas
    FROM Colleges COL
    JOIN Challenges CHAL
    ON CHAL.college_id = COL.college_id
    JOIN Submission_Stats ss
    ON ss.challenge_id = CHAL.challenge_id
    GROUP BY COL.contest_id
)

SELECT CON.*,
       s.ts, s.tas,
       v.tv, v.tuv
FROM Contests CON
JOIN vieu v
ON v.contest_id = CON.contest_id
JOIN submission s
ON s.contest_id = v.contest_id
WHERE s.ts != 0 OR
      s.tas != 0 OR
      v.tv != 0 OR
      v.tuv != 0
ORDER BY CON.contest_id;