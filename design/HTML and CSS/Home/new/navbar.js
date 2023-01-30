
var x = document.getElementsByClassName("ul");
window.addEventListener('resize', nav_hide);

function nav_hide(){
    if (window.innerWidth <= 480){
        for (i=0; i < x.length; i++) {
            x[i].style.display = "none";
        }
    }
    else{
        for (i=0; i < x.length; i++) {
            x[i].style.display = "";
        }
    }
}


let btn = document.querySelector(".fa")
function hamburger_toggle() {
    console.log(x)
    for (i=0; i < x.length; i++) {
        if (x[i].style.display === "") {
            x[i].style.display = "none";
        } else {
            x[i].style.display = "";
        }
    }
}
btn.addEventListener("click", hamburger_toggle);