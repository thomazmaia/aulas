// SELEÇÃO DE ELEMENTOS NO D.O.M:

// getElementById - Selecionar um elemento pelo ID:
var estrutura1 = document.getElementById("minhaDiv");

console.log("getElementById:");
console.log(estrutura1.innerText);
console.log(estrutura1.textContent);
console.log("---------------------");

// getElementsByClassName - Seleciona elementos pela classe;
var elementos = document.getElementsByClassName("minhaClasse");
console.log("getElementsByClassName:");
console.log(`Quantidade de elementos: ${elementos.length}`);
console.log(elementos[0].innerText);
console.log(elementos[1].textContent);
console.log("---------------------");
console.log("getElementsByClassName:");
for (let i = 0; i < elementos.length; i++){
    console.log(elementos[i].innerText);
}
console.log("-x-x-x-x-x-x-x-x-x-x-");

// querySelector - Seleciona o primeiro elemento com o seletor fornecido
console.log("querySelector: ");
let estrutura2 = document.querySelector("#minhaDiv");
console.log(estrutura2.innerText);
console.log(estrutura2.textContent);
console.log("---------------------");

// querySelectorAll - Seleciona todos os elementos com o seletor fornecido
elementos = document.querySelectorAll(".minhaClasse");
console.log("querySelectorAll:");
console.log(`Quantidade de elementos: ${elementos.length}`);
console.log(elementos[0].innerText);
console.log(elementos[1].textContent);
console.log("---------------------");
console.log("querySelectorAll:");
for (let i = 0; i < elementos.length; i++){
    console.log(elementos[i].innerText);
}
console.log("---------------------");