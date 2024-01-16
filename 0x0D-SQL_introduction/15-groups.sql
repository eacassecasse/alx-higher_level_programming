# Displays the score and amount of the record which have
# the same score in the table ``second_table`` in descending order
SELECT score, count(*) as number
FROM second_table
GROUP BY score
ORDER BY number DESC;
