const botao = document.querySelector("#botao-iniciar");
const mensagem = document.querySelector("#mensagem");

botao.addEventListener("click", function() {
    mensagem.textContent = "A disciplina começou! AGORA VAI!";

    botao.textContent = "BORA!!!";
    botao.disabled = true;
})