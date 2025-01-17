// Conversão entre tipos

let texto = "JavaScript";
let A = 1;
let B = "1";
let C = 3.14;
let D = "3.14";

console.log("--- Original:");
console.log(A + " tipo: " + typeof(A));
console.log(B + " tipo: " + typeof(B));
console.log(C + " tipo: " + typeof(C));
console.log(D + " tipo: " + typeof(D));

let novoA = A.toString();
let novoB = parseInt(B);
let novoC = C.toString();
let novoD = parseFloat(D);

console.log("--- Convertido (parseado):")
console.log(novoA + " tipo: " + typeof(novoA));
console.log(novoB + " tipo: " + typeof(novoB));
console.log(novoC + " tipo: " + typeof(novoC));
console.log(novoD + " tipo: " + typeof(novoD));

let novoTexto = parseInt(texto);
console.log(novoTexto + " tipo: " + typeof(novoTexto));