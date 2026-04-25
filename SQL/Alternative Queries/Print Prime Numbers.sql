# Written in MySQL Language

WITH RECURSIVE divisors AS (
    SELECT 2 AS N
    union all
    SELECT N + 1 N
    FROM divisors 
    WHERE N < 1000
),
primeNumbers AS (
    SELECT N 
    FROM divisors D1
    WHERE NOT EXISTS (
        SELECT 1 
        FROM divisors D2 
        WHERE (D2.N > 1 and D2.N < D1.N) and (D1.N % D2.N = 0)
    )
)
SELECT GROUP_CONCAT(N SEPARATOR '&') 
FROM primeNumbers;