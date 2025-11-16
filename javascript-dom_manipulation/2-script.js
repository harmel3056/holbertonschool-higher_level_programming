// Adds the class 'red' to the header when
// the user clicks on the tag with id red_header
const selector = document.getElementById('red_header');
const colourChange = document.querySelector('header');

selector.addEventListener('click', function () {
  colourChange.classList.add('red');
});
