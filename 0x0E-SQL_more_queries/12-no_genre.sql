-- Displays the list of TV Shows without a genre
SELECT _show.title, _genre.genre_id
FROM tv_shows _show
         LEFT OUTER JOIN (tv_show_genres _genre)
                         ON _show.id = _genre.show_id
WHERE _genre.genre_id IS NULL
ORDER BY _show.title, _genre.genre_id;
