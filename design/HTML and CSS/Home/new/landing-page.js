let dot_1 = document.querySelector('.dot-1');
let dot_2 = document.querySelector('.dot-2');
let para_1 = document.querySelector('.para-1');
let para_2 = document.querySelector('.para-2');

let holder_1 = dot_1.style.backgroundColor;
let holder_2 = dot_2.style.backgroundColor;

holder_1 = '#E6CA97';
holder_2 = '#FFFDD0';
console.log(holder_1)

dot_1.addEventListener('click', hide_1)
dot_2.addEventListener('click', hide_2)

function hide_1(){
    para_1.style.display = "block";
    para_2.style.display = "none";
    dot_1.style.backgroundColor = holder_1;
    dot_2.style.backgroundColor = holder_2;
}
function hide_2(){
    para_1.style.display = "none";
    para_2.style.display = "block";
    dot_1.style.backgroundColor = holder_2;
    dot_2.style.backgroundColor = holder_1;
}