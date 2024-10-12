SELECT T1.start_date, T2.end_date
FROM (
    SELECT start_date, ROW_NUMBER() OVER (ORDER BY start_date) row_num
    FROM projects
    WHERE start_date NOT IN (SELECT end_date FROM projects)
) T1 JOIN  (
    SELECT end_date, ROW_NUMBER() OVER (ORDER BY end_date) row_num
    FROM projects
    WHERE end_date NOT IN (SELECT start_date FROM projects)
) T2 ON T1.row_num=T2.row_num
ORDER BY
    T2.end_date - T1.start_date,
    T1.start_date;