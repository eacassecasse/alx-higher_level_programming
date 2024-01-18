-- Displays the list of cities with the corresponding
-- state names
SELECT _c.id, _c.name, _s.name
FROM cities _c
         INNER JOIN (states _s)
                    ON _c.state_id = _s.id
ORDER BY _c.id;

