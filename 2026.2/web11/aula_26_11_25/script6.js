let titulo = document.getElementById("titulo");

function mudar_titulo(e){
    if (titulo.textContent == "Exemplo") {
        titulo.textContent = "Titulo alterado!";
    } else {
        titulo.textContent = "Exemplo";
    }
}