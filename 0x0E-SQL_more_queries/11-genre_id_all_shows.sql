-- Displays the list of TV Shows with their own
-- genres
SELECT _show.title, _genre.genre_id
FROM tv_shows _show
         LEFT JOIN (tv_show_genres _genre)
                    ON _show.id = _genre.show_id
ORDER BY _show.title, _genre.genre_id;

