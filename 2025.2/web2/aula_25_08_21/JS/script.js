// Declaração de tipos diferentes:
var texto = "JavaScript";
var A = 1;
var B = "1";
var C = 3.14;
var D = "3.14";

console.log("--- Original:");
console.log(texto + " tipo " + typeof(texto));
console.log(A + " tipo " + typeof(A));
console.log(B + " tipo " + typeof(B));
console.log(C + " tipo " + typeof(C));
console.log(D + " tipo " + typeof(D));

// Conversão entre tipos:
let novoA = A.toString();
let novoB = parseInt(B);
let novoC = C.toString();
let novoD = parseFloat(D);

console.log("--- Convertido:");
console.log(novoA + " tipo " + typeof(novoA));
console.log(novoB + " tipo " + typeof(novoB));
console.log(novoC + " tipo " + typeof(novoC));
console.log(novoD + " tipo " + typeof(novoD));

// let novoTexto = parseInt(texto);
// console.log("--- Convertido/parseado:");
// console.log(novoText + " tipo " + typeof(novoTexto));

// Lendo algo do usuário
var nome = prompt("Digite seu nome: ");
console.log("Olá " + nome);
console.log(typeof(nome));

var N = prompt("Digite um número: ")
var X = parseFloat(N);
console.log(`Tipo de N: ${typeof(N)}`);
console.log(`Tipo de X: ${typeof(X)}`);