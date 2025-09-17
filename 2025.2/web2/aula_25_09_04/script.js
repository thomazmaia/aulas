function alterar(){
    let caixa = document.getElementById("caixa"); // Tem que ser GETELEMENTBYID!
    caixa.style.backgroundColor = "Red";
    caixa.style.width = "10px";
    caixa.innerText = "Mudei!";
}

function resetar(){
    let caixa = document.getElementById("caixa"); // Tem que ser GETELEMENTBYID!
    caixa.style.backgroundColor = "Yellow";
    caixa.style.width = "200px";
    caixa.innerText = "Olá Mundo";
}