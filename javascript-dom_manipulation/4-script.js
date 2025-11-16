// Adds a li element to a list when
// the user clicks on the element id add_item
const ToggleAddItem = document.getElementById('add_item');
const ul = document.querySelector('.my_list');

ToggleAddItem.addEventListener('click', function () {
  const NewItem = document.createElement('li');
  NewItem.textContent = 'Item';
  ul.appendChild(NewItem);
});
