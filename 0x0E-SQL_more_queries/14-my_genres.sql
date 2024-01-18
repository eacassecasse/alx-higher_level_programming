-- Displays the list of existing genre related to the
-- show Dexter
SELECT _genre.name
FROM tv_genres _genre
         INNER JOIN (tv_show_genres _show_genre, tv_shows _show)
                    ON (_genre.id = _show_genre.genre_id AND _show.id = _show_genre.show_id)
WHERE _show.title = 'Dexter'
ORDER BY _genre.name;
