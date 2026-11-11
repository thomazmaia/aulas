alert("Olá mundo de novo!");
console.log("Olá mundo de novo!"); // print()

// Saída de dados
console.log("----------");
console.log("Saída de dados");
console.log(10);
console.log("20");
console.log("Texto qualquer");

// Variáveis
console.log("----------");
console.log("Variáveis");
var X = 10;   // Não é mais usado
let Y = 20;   // Variável que varia
const Z = 30; // Variável que não varia
console.log(X, Y, Z);

// Tipos de dados
console.log("----------");
console.log("Tipos de dados");
let A = 10;
let B = 10.5;
let C = "aaaa";
let D = true;

console.log(typeof(A));
console.log(typeof(B));
console.log(typeof(C));
console.log(typeof(D));
console.log(typeof(E));

// Tipagem de dados
console.log("----------");
console.log("Tipagem");

let N = 99;
console.log(N, typeof(N));
N = "noventa e nove"
console.log(N, typeof(N));
N = "99";
console.log(N, typeof(N));
N = Number(N); // Conversão de str -> number
console.log(N, typeof(N));

// Formatação
console.log("----------");
console.log("Formatação");

console.log("Texto aqui");
console.log(99);
console.log("Aqui é texto", 18);
console.log("Olá", "Mundo!");
console.log("Olá" + "Mundo!");
let nome = "thomaz";
console.log(`Olá ${nome}`);

// Operadores aritméticos
console.log("----------");
console.log("Operadores aritméticos");
let a = 10;
let b = 3;
console.log(a + b); // 13
console.log(a - b); // 7
console.log(a * b); // 30
console.log(a / b); // 3.33
console.log(a ** b); //1000
console.log(a % b); // 1

// Operadores relacionais
console.log("----------");
console.log("Operadores relacionais");
console.log(a > b);  // true
console.log(a >= b); // true
console.log(a < b);  // false
console.log(a <= b); // false
console.log(a == b); // false
console.log(a != b); // true

// Operadores lógicos
console.log("----------");
console.log("Operadores lógicos");
console.log((10 > 3) && (2 != 4)); // and
console.log((0 > 3) || (2 != 2)); // or
console.log( !(3 > 0) ); // not

// Condicionais
console.log("----------");
console.log("Condicionais");
let idade = 20;

if (idade >= 18) {
    console.log("Adulto");
} else if (idade >= 13) {
    console.log("Adolescente");
} else {
    console.log("Criança");
}

// Laços
console.log("----------");
console.log("Laço while");
let contador = 5;

while (contador > 0){
    console.log(contador);
    contador--; //contador -= 1;
}

console.log("Laço for");

for (let i = 1; i <= 5; i++){
    console.log(i);
}