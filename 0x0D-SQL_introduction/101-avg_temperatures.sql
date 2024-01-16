-- Computes and display the average temperatures
-- grouped by city in descending order
SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
