// Adds the class 'red' to the header when
// the user clicks on the tag with id toggle_header
const ClassToggle = document.getElementById('toggle_header');
const ColourChange = document.querySelector('header');

ClassToggle.addEventListener('click', function () {
  if (ColourChange.classList.contains('green')) {
    ColourChange.classList.replace('green', 'red');
  } else if (ColourChange.classList.contains('red')) {
    ColourChange.classList.replace('red', 'green');
  }
});
