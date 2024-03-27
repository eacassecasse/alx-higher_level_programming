#!/usr/bin/node
const request = require('request');
const searchVal = 'https://swapi-api.alx-tools.com/api/people/18/'

request(process.argv[2],
    (error, response, body) => {
        if (!error) {
            const films = JSON.parse(body).results;
            console.log(films.reduce((counter, film) => {
                return film.characters.find((char) => char.endsWith('/18/'))
                    ? counter + 1 : counter;
            }, 0));
        }
    });
