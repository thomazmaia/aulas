// COMO ACESSAR ELEMENTOS
// querySelectorAll() - Seleciona todos os elementos

let elementos = document.querySelectorAll(".minhaClasse");

console.log("Array de elementos:");
console.log(elementos);

let texto1 = elementos[0].textContent;
let texto2 = elementos[1].textContent;
console.log("Textos dos elementos:");
console.log(texto1);
console.log(texto2);