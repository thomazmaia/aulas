let display = document.getElementById("display");    

function pressionar(valor) {
    if(display.innerHTML == "0") {
        display.innerHTML = valor;
    } else {
        display.innerHTML += valor;
    }
}

function limpar() {
    display.innerHTML = "0";
}

function calcular(){
    var conta = display.innerHTML;
    var resultado = eval(conta);
    display.innerHTML = resultado;
}