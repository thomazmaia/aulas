// AULA DE ONTEM: SELECIONANDO ELEMENTOS
// getElementById - Selecionar um elemento pelo ID:
// getElementsByClassName - Seleciona elementos pela classe;
// querySelector - Seleciona o primeiro elemento com o seletor fornecido
// querySelectorAll - Seleciona todos os elementos com o seletor fornecido

// AULA DE HOJE: MANIPULANDO CONTEÚDOS
var obj_txt = document.querySelector(".txt");

obj_txt.textContent = "OLÁ MUNDO";

var obj_img = document.querySelector("#img");

console.log(obj_img.getAttribute("src"));

obj_img.setAttribute("src", "img/volvo.jpg");