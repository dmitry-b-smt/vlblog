//new article
const pageInputField = document.getElementById("id_title");
const pageInputFieldPlaceholder = pageInputField.placeholder

pageInputField.addEventListener("focus", function () {
    pageInputField.placeholder = "";
});
pageInputField.addEventListener("blur", function () {
    pageInputField.placeholder = pageInputFieldPlaceholder;
});

const pageInputArea = document.getElementsByClassName('creator__text-area');
const pageInputAreaPlaceholder = document.querySelector('.note-placeholder')
console.log(pageInputAreaPlaceholder.class);

pageInputArea.addEventListener("focus", function () {
    pageInputFieldPlaceholder.style.visibility = "hidden";
});
pageInputField.addEventListener("blur", function () {
    pageInputFieldPlaceholder.style.visibility = "visible";
});