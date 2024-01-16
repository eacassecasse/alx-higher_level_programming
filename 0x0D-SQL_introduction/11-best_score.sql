# List only the score and name which are >= 10 of the table
# ``second_table`` order by score descending
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
