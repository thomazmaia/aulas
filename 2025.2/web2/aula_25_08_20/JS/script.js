// Declaração de variáveis:
var nome;
nome = "Thomaz Maia";

// "print" no console:
console.log(nome);
console.log("Olá " + nome); // Concatenação de strings
console.log(`Olá ${nome}`); // Template Strings (acento agudo: `)

console.log("----------------")

// Exercício: Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias.
let preco_livro = 24.95;
let desconto = 40/100;

let valor_desconto = preco_livro * desconto;
let preco_livro_com_desconto = preco_livro - valor_desconto;

console.log("Desconto = " + valor_desconto);
console.log("Livro com desconto = " + preco_livro_com_desconto);

let numero_copias = 60;

let preco_60_copias = numero_copias * preco_livro_com_desconto;

console.log(`Preço para as ${numero_copias} cópias = R$${preco_60_copias}`);

let preco_transporte = 3.00 + 0.75*(numero_copias - 1);

let custo_total = preco_60_copias + preco_transporte;

console.log(`Custo total das ${numero_copias} cópias = R$${custo_total}`);

