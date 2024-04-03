$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
  $('UL#list_movies').append(...data.results.map(mov => `<li>${mov.title}</li>`));
});
