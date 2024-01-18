-- Displays the list of TV Shows with at least one
-- genre
SELECT _show.title, _genre.genre_id
FROM tv_shows _show
         INNER JOIN (tv_show_genres _genre)
                    ON _show.id = _genre.show_id
ORDER BY _show.title, _genre.genre_id;

