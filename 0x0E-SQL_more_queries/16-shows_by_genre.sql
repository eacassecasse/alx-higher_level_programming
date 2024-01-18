-- Displays the list of TV Shows with their own
-- genres
SELECT _show.title, _genre.name
FROM tv_shows _show
         LEFT JOIN (tv_show_genres _show_genre, tv_genres _genre)
                   ON (_show.id = _show_genre.show_id AND _genre.id= = _show_genre.genre_id)
ORDER BY _show.title, _genre.genre_id;

