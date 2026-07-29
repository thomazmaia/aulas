const botao = document.querySelector("#botao-iniciar");
const mensagem = document.querySelector("#mensagem");

botao.addEventListener("click", function() {
    mensagem.textContent = "Começou!!!!!";

    botao.textContent = "Semestre Iniciado!"
    botao.disabled = true;
});