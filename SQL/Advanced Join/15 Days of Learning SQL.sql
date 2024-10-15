WITH SubList AS (Select Submission_date, hacker_id, Rank() Over(Partition by hacker_id order by submission_date)AS HRank From (Select Submission_date, hacker_id, Count(hacker_id) As HCount From Submissions Group By Submission_date, hacker_id) SubQ1),

DateAnchor AS (Select Distinct (Submission_date) As Sub_date, Right(Submission_date,2) As Day From Submissions),

SubCount AS (Select Submission_date, Hrank, Count(hacker_id) AS SubC From SubList Group by Submission_date, HRank),

DailySub AS (Select S.Submission_date, S.Hrank, S.SubC, D.Day From SubCount S Join DateAnchor D ON S.Hrank = D.Day and S.Submission_date = D.Sub_date),

MSubm As (Select Submission_date, hacker_id, Name, IDCount, Rank() Over (Partition by Submission_date Order By IDCount Desc, hacker_id) AS RankC From (Select S.Submission_date, H.Name, S.hacker_id, Count(S.hacker_id) As IDCount From Submissions S Join Hackers H On S.hacker_id = H.hacker_id Group By S.Submission_date, H.name, S.hacker_id) SubQ2)

Select D.Submission_date, D.SubC, M.hacker_id, M.Name From DailySub D Join MSubm M On D.Submission_date = M.Submission_date Where M.RankC = 1;