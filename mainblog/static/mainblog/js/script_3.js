//recovery password
const pageText = document.querySelector('label');
const pageInputField = document.querySelector('input');

pageText.setAttribute('class', 'registration__text');
pageInputField.setAttribute('class', 'registration__form-field');
pageInputField.setAttribute('placeholder', 'Введите e-mail*');

const pageInputFieldPlaceholder = pageInputField.placeholder;
console.log(pageInputFieldPlaceholder);

pageInputField.addEventListener("focus", function (e) {
    pageInputField.placeholder = "";
});
pageInputField.addEventListener("blur", function (e) {
    pageInputField.placeholder = pageInputFieldPlaceholder;
});