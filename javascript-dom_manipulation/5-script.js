// Updates the header text when
// the user clicks on the element id update_header
const ToggleUpdateHeader = document.getElementById('update_header');
const Header = document.querySelector('header');

ToggleUpdateHeader.addEventListener('click', function () {
  Header.textContent = 'New Header!!!';
});
