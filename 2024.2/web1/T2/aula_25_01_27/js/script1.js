// ACESSANDO ELEMENTOS DO D.O.M.
// getElementById - Seleciona um elemento pelo ID
var elemento = document.getElementById("titulo");
var conteudo = elemento.textContent;
console.log(conteudo)

// getElementByClassName - Seleciona elementos pela classe
var lista_de_classes = document.getElementsByClassName("texto");
var texto1 = lista_de_classes[0].textContent;
var texto2 = lista_de_classes[1].textContent;
console.log(texto1);
console.log(texto2);

console.log("-------------")

// querySelector - Seleciona o elemento pela tag
var objeto = document.querySelector("#titulo");
var lista_de_objetos = document.querySelectorAll(".texto");
console.log(objeto.textContent);
console.log(lista_de_objetos[0].textContent);
console.log(lista_de_objetos[1].textContent);
