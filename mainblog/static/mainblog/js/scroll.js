//scroll to recent articles

const scrollRecent = document.getElementById('articles');
const arrowBlog = document.querySelector('.blog__arrow-link');

arrowBlog.addEventListener("click", function (e) {
    e.preventDefault();
    scrollRecent.scrollIntoView({
       behavior: "smooth"
    });
});


//home fade-in while scroll down


function onEntry(entry) {
  entry.forEach(change => {
    if (change.isIntersecting) {
      change.target.classList.add('content__articles-show');
    } else {
        change.target.classList.remove('content__articles-show');
    }
  });
}
let options = { threshold: [0.1] };
let observer = new IntersectionObserver(onEntry, options);
let elements = document.querySelectorAll('.content__articles');
for (let elm of elements) {
  observer.observe(elm);
}