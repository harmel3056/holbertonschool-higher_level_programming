// Changes the colour of the header to red when
// the user clicks on the tag with id red_header
const Selector = document.getElementById('red_header');
const ColourChange = document.querySelector('header');

Selector.addEventListener('click', function () {
  ColourChange.style.color = '#FF0000';
});
