// Retrieves movie titles from URL and
// lists them under list_movies
(async function () {
  try {
    const response = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');

    if (!response.ok) {
      throw new Error(`error: ${response.status}`);
    }

    const data = await response.json();
    const movies = data.results;
    const ul = document.getElementById('list_movies');

    for (const movie of movies) {
      const list = document.createElement('li');
      list.textContent = movie.title;
      ul.appendChild(list);
    }
  } catch (error) {
    console.error(error);
  }
})();
