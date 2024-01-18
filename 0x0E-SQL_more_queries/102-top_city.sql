-- Computes and display the average temperatures
--  of July and August grouped by temperatures
-- in descending order
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month = 7 or month = 8
GROUP BY city
ORDER BY avg_temp DESC LIMIT 3;

