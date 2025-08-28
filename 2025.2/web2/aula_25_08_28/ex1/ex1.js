// Ao clicar no botão #btn o título <h1> deve mudar para "TCHAU, MUNDO"
// Toda vez que clicar no botão, o título deve mudar. De olá para tchau, de tchau para olá.


function troca(e) {
    var titulo = document.querySelector("#titulo");
    if (titulo.textContent == "OLÁ, MUNDO!") {
        titulo.textContent = "TCHAU, MUNDO";
    } else {
        titulo.textContent = "OLÁ, MUNDO!";
    }   
}
