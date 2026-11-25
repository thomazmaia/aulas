// COMO ACESSAR ELEMENTOS
// querySelector - Pega o elemento com a tag fornecida
// querySelectorAll - Pega oS elementoS com a tag fornecida

let elemento1 = document.querySelector("#meuDiv");
console.log("Elemento: ");
console.log(elemento1);

let texto = elemento1.textContent;
console.log("Texto do elemento:")
console.log(texto);


let elementos = document.querySelectorAll(".minhaClasse");
console.log("Elementos");
console.log(elementos);

let texto1 = elementos[0].textContent;
let texto2 = elementos[1].textContent;

console.log("Texto do elemento 1:");
console.log(texto1);
console.log("Texto do elemento 2:");
console.log(texto2);