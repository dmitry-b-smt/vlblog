//  registration form, login form, recover form:
const formInputFields = document.querySelectorAll('.registration__form-field');

formInputFields.forEach(function (item, i, formInputFields){
    let itemPlaceholder = item.placeholder;
    item.addEventListener("focus", function (e) {
        item.placeholder = "";
    });
    item.addEventListener("blur", function (e) {
        item.placeholder = itemPlaceholder;
    });
});