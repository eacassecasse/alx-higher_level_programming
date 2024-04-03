#!/usr/bin/node
const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
  (error, response, body) => {
    if (error) {
      console.log(error);
    } else if (response.statusCode === 200) {
      const film = JSON.parse(body);
      console.log(film.title);
    } else {
      console.log('Error code: ', response.statusCode);
    }
  });
