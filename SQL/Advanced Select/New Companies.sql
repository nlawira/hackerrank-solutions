SELECT C.company_code, C.founder, count(distinct(L.lead_manager_code)), count(distinct(S.senior_manager_code)), count(distinct(M.manager_code)), count(distinct(E.employee_code))
FROM Company AS C
INNER JOIN Lead_Manager AS L
ON C.company_code = L.company_code
INNER JOIN Senior_Manager AS S
ON C.company_code = S.company_code
INNER JOIN Manager AS M
ON C.company_code = M.company_code
INNER JOIN Employee AS E
ON C.company_code = E.company_code
GROUP BY C.company_code, C.founder
ORDER BY C.company_code ASC;