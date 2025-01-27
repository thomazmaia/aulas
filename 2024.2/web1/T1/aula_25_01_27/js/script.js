function soma() {
    let valor1 = parseInt(document.querySelector("#val1").value);
    let valor2 = parseInt(document.querySelector("#val2").value);
    let soma = valor1 + valor2;
    document.querySelector("#resp").textContent = "Resposta: " + soma;
}

function subtracao() {
    let valor1 = parseInt(document.querySelector("#val1").value);
    let valor2 = parseInt(document.querySelector("#val2").value);
    let soma = valor1 - valor2;
    document.querySelector("#resp").textContent = "Resposta: " + soma;
}