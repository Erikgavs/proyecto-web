
// SCROLL DE LA PÁGINA PRINCIPAL
function scrollToSection() {
    document.getElementById('ancla').scrollIntoView({
        behavior: "smooth"
    })
}

document.querySelector(".card").addEventListener("click", function(){
    window.location.href = "bebida1.html";
});