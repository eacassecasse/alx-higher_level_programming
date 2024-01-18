-- Displays the list of cities that are related to the
-- record ``name = California`` in the table ``states``
SELECT cities.id, cities.name
FROM states,
     cities
WHERE cities.state_id = states.id
  AND states.name = 'California'
ORDER BY cities.id;

