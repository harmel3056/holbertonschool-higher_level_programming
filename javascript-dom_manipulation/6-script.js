// Retrieves name from URL and returns
// it within the character tag
(async function () {
  try {
    const response = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');

    if (!response.ok) {
      throw new Error(`error: ${response.status}`);
    }

    const data = await response.json();
    const name = data.name;
    const tagId = document.getElementById('character');

    tagId.textContent = name;
  } catch (error) {
    console.error(error);
  }
})();
