// Adds the class 'red' to the header when
// the user clicks on the tag with id toggle_header
const classToggle = document.getElementById('toggle_header');
const colourChange = document.querySelector('header');

classToggle.addEventListener('click', function () {
  if (colourChange.classList.contains('green')) {
    colourChange.classList.replace('green', 'red');
  } else if (colourChange.classList.contains('red')) {
    colourChange.classList.replace('red', 'green');
  }
});
