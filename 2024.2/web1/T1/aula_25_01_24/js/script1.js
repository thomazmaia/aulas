// Acessando pelo ID - getElementById
let elemento = document.getElementById("meuDiv");
console.log(elemento.textContent);

// Acessando pela classe - getElementsByClassName
let elementos = document.getElementsByClassName("minhaClasse");
console.log(elementos[0].textContent);
console.log(elementos[1].textContent);

// Acessando o elemento pela tag - querySelector
let objeto1 = document.querySelector("#meuDiv");
console.log(objeto1.textContent);

// Acessando o elemento pela tag - querySelectorAll
let objetos = document.querySelectorAll(".minhaClasse")
console.log(objetos[0].textContent)
console.log(objetos[1].textContent)