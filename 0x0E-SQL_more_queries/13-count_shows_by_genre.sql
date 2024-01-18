-- Displays the list of existing genre with the amount
-- of shows linked to each one, excluding those that doesn't
-- have a linked show
SELECT tv_genres.name AS 'genre', COUNT(tv_show_genres.genre_id) AS 'number_of_shows'
FROM tv_genres
         RIGHT JOIN tv_show_genres
                    ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;