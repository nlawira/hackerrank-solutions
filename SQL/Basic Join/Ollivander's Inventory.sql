WITH CTE AS (
    SELECT 
        code,
        power,
        min(coins_needed) as min_coins
    FROM
        Wands
    GROUP BY code, power
)

SELECT
    t1.id,
    t3.age,
    t2.min_coins,
    t1.power
FROM
    Wands AS t1
INNER JOIN CTE AS t2
ON 
    t1.code = t2.code AND
    t1.power = t2.power AND 
    t1.coins_needed = t2.min_coins
LEFT JOIN Wands_Property AS t3
ON t1.code = t3.code
WHERE
    t3.is_evil = 0
ORDER BY
    t1.power desc,
    t3.age desc;