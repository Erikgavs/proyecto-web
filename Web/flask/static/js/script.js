
// SCROLL DE LA PÁGINA PRINCIPAL
function scrollToSection() {
    document.getElementById('ancla').scrollIntoView({
        behavior: "smooth"
    })
}

// COMPROBACIÓN DE QUE LAS DOS CONTRASEÑAS DEL FORM (REGISTER) ES CORRECTA

const form = document.querySelector('.formulario-register');
const password1 = document.querySelector('.input-password1');
const password2 = document.querySelector('.input-password2');
const mensajeError = document.querySelector('.mensaje-error');

form.addEventListener('submit', function(event) {
    if (password1.value !== password2.value) {
        event.preventDefault();
        mensajeError.textContent = "Las contraseñas no coinciden.";
    } else {
        mensajeError.textContent = "";
    }
});

// REVISAR APARTADO Y ENCARGARME DE ENTENDERLO BIEN BIEN