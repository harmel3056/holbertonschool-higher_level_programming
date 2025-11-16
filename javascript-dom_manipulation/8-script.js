// Retrieves the french value for hello
document.addEventListener('DOMContentLoaded', async () => {
  try {
    const response = await fetch('https://hellosalut.stefanbohacek.com/?lang=fr');

    if (!response.ok) {
      throw new Error(`error: ${response.status}`);
    }

    const data = await response.json();
    document.getElementById('hello').textContent = data.hello;
  } catch (error) {
    console.error(error);
  }
})();
