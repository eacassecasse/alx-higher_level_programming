-- Displays the list of TV Shows only of the Comedy
-- genre
SELECT _show.title
FROM tv_shows _show
         INNER JOIN (tv_show_genres _show_genre, tv_genres _genre)
                    ON (_show.id = _show_genre.show_id AND _genre.id = _show_genre.genre_id)
WHERE _genre.name = 'Comedy'
ORDER BY _show.title;
