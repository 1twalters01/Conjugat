let main_container = document.querySelector('.main-container');
let background = document.querySelector('.background');

background.style.height = main_container.offsetHeight + 'px';
addEventListener("scroll", (event) => {
    background.style.height = main_container.offsetHeight + 'px'
}
);