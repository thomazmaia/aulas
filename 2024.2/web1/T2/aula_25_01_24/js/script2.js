// Código para cálculo de compra e desconto.

var produto = "Celular";
var preco = 2500;
var quantidade = 4;
var desconto = 15;

let precoTotal = preco * quantidade;
let descontoCalculado = precoTotal * desconto/100;
let precoFinal = precoTotal - descontoCalculado;

console.log("Desconto calculado: R$" + descontoCalculado);
console.log(`Preço final: R$${precoFinal}`);