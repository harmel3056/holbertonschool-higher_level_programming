// Adds a li element to a list when
// the user clicks on the element id add_item
const toggleAddItem = document.getElementById('add_item');
const ul = document.querySelector('.my_list');

toggleAddItem.addEventListener('click', function () {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  ul.appendChild(newItem);
});
