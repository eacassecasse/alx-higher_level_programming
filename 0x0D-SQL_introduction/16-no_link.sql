# Displays only the score an name to the records that
# has names on the table ``second_table``
SELECT score, name
FROM second_table
WHERE name <> ''
ORDER BY score DESC;
