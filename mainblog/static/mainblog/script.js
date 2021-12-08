const commentFormInput = document.querySelector('textarea');
const commentFormInputPlaceholder = commentFormInput.placeholder;

commentFormInput.addEventListener("focus", function (e) {
    commentFormInput.placeholder = "";
});
commentFormInput.addEventListener("blur", function (e) {
    commentFormInput.placeholder = commentFormInputPlaceholder;
});
console.log(commentFormInputPlaceholder);