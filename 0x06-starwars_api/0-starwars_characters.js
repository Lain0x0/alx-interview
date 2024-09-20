#!/usr/bin/node
/** 
 * Star Wars Alx Interview
*/

const request = require('request');

const fetch = (urlbase) => new Promise((resolve, reject) => {
  request(urlbase, (err, _, body) => {
    if (err) reject(err);
    else resolve(JSON.parse(body));
  });
});

const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./star_wars_characters.js <movie_id>');
  process.exit(1);
}

fetch(`https://swapi.dev/api/films/${movieId}/`)
  .then(film => Promise.all(film.characters.map(fetch)))
  .then(characters => characters.forEach(character => console.log(character.name)))
  .catch(console.error);