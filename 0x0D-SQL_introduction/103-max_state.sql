-- Computes and display the max temperatures
-- grouped by state in descending order
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC;
