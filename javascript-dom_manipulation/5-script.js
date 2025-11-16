// Updates the header text when
// the user clicks on the element id update_header
const toggleUpdateHeader = document.getElementById('update_header');
const header = document.querySelector('header');

toggleUpdateHeader.addEventListener('click', function () {
  header.textContent = 'New Header!!!';
});
