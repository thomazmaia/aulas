// COMO ACESSAR ELEMENTOS
// getElementById() - Pega o elemento pelo ID
// getElementsByClassName() - Pega oS elementoS pela CLASS

let elemento1 = document.getElementById("meuDiv");
console.log("Elemento: ");
console.log(elemento1);

let texto = elemento1.textContent;
console.log("Texto do elemento:")
console.log(texto);


let elementos = document.getElementsByClassName("minhaClasse");
console.log("Elementos");
console.log(elementos);

let texto1 = elementos[0].textContent;
let texto2 = elementos[1].textContent;

console.log("Texto do elemento 1:");
console.log(texto1);
console.log("Texto do elemento 2:");
console.log(texto2);