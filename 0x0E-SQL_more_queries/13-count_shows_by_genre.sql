-- Displays the list of existing genre with the amount
-- of shows linked to each one, excluding those that doesn't
-- have a linked show
SELECT _genre.name, count(*) as number_of_shows
FROM tv_genres _genre
         INNER JOIN (tv_show_genres _show_genre, tv_shows _show)
                    ON (_genre.id = _show_genre.genre_id AND _show.id = _show_genre.show_id)
WHERE _show_genre.show_id IS NOT NULL
GROUP BY _genre.name
ORDER BY number_of_shows DESC;
