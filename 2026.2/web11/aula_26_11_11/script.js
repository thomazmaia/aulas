alert("Olá, mundo!");
console.log("Olá, mundo!"); // print("Olá, mundo!")

// Saída
console.log("----------");
console.log("Saída");
console.log(10);
console.log(10 + 5);


// Variáveis
console.log("----------");
console.log("Variáveis");
var X = 10; // Não se usa mais
let Y = 20; // Variável que varia
const Z = 30; // Variável que não varia
console.log(X, Y, Z);

// Tipos de dados
console.log("----------");
console.log("Tipos de dados");

let A = 10;     // number
let B = 10.5;   // number
let C = "aaa";  // string
let D = true;   // boolean

console.log(typeof(A));
console.log(typeof(B));
console.log(typeof(C));
console.log(typeof(D));
console.log(typeof(E));

// Tipagem
console.log("----------");
console.log("Tipagem");

let N = 99;
console.log(N, typeof(N));
N = "noventa e nove";
console.log(N, typeof(N));
N = "99";
console.log(N, typeof(N));
N = Number(N); // conversão
console.log(N, typeof(N));

// Formatação
console.log("----------");
console.log("Formatação");
let nome = "Thomaz";
console.log("Olá", nome);
console.log("Olá " + nome);
console.log(`Olá ${nome}`);

// Operadores
console.log("----------");
console.log("Operadores");
let a = 10;
let b = 3;
console.log(a + b);  // 13
console.log(a - b);  // 7
console.log(a * b);  // 30
console.log(a / b);  // 3.33
console.log(a % b);  // 1
console.log(a ** b); // 1000
console.log(Math.floor(a / b)); // 3
console.log(Math.ceil(a / b)); // 4

// Relacionais
console.log("----------");
console.log("Operadores Relacionais");
console.log(a > b);   // true
console.log(a >= b);  // true
console.log(a < b);   // false
console.log(a <= b);  // false
console.log(a == b);  // false
console.log(a != b);  // true

// Lógicos
console.log("----------");
console.log("Operadores Lógicos");
console.log((a > b) && (3 > 10)); // and
console.log((a < b) || (3 > 10)); // or
console.log(!(false)); // not

// Condicionais (if/else if/else)
console.log("----------");
console.log("Condicionais");
let idade = 10;

if (idade >= 18){
    console.log("Adulto");
} else if (idade >= 13){
    console.log("Adolescente");
} else {
    console.log("Criança");
}

// Laços (while e for)
console.log("----------");
console.log("Laço while");
let contador = 5;

while (contador > 0){
    console.log(contador);
    contador--; //contador -= 1; // contador = contador - 1
}

console.log("Laço for");
for (let i = 1; i <= 5; i++){
    console.log(i);
}