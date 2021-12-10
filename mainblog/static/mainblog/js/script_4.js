//profile
// buttonInput.classList.add('button', 'profile__button');
// buttonInput.style.display = 'none';

const buttonInput = document.getElementById('id_img');
console.log(buttonInput);
buttonInput.style.opacity = 0;

const formInputFields = document.querySelectorAll('.registration__form-field');

formInputFields.forEach(function (item, i, formInputFields) {
    let itemPlaceholder = item.placeholder;
    item.addEventListener("focus", function () {
        item.placeholder = "";
    });
    item.addEventListener("blur", function () {
        item.placeholder = itemPlaceholder;
    });
});