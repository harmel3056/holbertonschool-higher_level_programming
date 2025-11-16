// Adds the class 'red' to the header when
// the user clicks on the tag with id red_header
const Selector = document.getElementById('red_header');
const ColourChange = document.querySelector('header');

Selector.addEventListener('click', function () {
  ColourChange.classList.add('red');
});
