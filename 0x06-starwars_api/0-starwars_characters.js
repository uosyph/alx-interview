#!/usr/bin/node

const request = require('request');

let data;
let characters = [];
const movieId = process.argv.slice(2)[0];

// Function to get the character name using the character ID
function getCharacterName (characterId) {
  return new Promise((resolve, reject) => {
    request(characterId, (err, res, body) => {
      if (err) reject(err);
      else resolve(JSON.parse(body).name);
    });
  });
}

// Function to get character IDs for a given movie ID
function getCharacterId (movieId) {
  request(`https://swapi-api.alx-tools.com/api/films/${movieId}`,
    async function (err, res, body) {
      if (err) console.error(err);
      else {
        data = JSON.parse(body);
        characters = data.characters;

        // Loop through character IDs and get their names
        for (let id = 0; id < characters.length; id++) {
          const characterName = await getCharacterName(characters[id]);
          console.log(characterName);
        }
      }
    });
}

getCharacterId(movieId);
