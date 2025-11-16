// Changes the colour of the header to red when
// the user clicks on the tag with id red_header
const selector = document.getElementById('red_header');
const colourChange = document.querySelector('header');

selector.addEventListener('click', function () {
  colourChange.style.color = '#FF0000';
});
