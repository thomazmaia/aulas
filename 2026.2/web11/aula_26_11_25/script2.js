// COMO ACESSAR ELEMENTOS
// getElementsByClassName() - Seleciona todos os elementos pela classe

let elementos = document.getElementsByClassName("minhaClasse");

console.log("Array de elementos:");
console.log(elementos);

let texto1 = elementos[0].textContent;
let texto2 = elementos[1].textContent;
console.log("Textos dos elementos:");
console.log(texto1);
console.log(texto2);