var expressao = "0";
var visor = document.getElementById("visor");

function mostrar(e) {
    if (expressao == 0) {
        expressao = e.target.innerText;
    } else {
        expressao = expressao + e.target.innerText;
    }
    atualiza_valor();    
}

function limpar(e) {
    expressao = "0";
    atualiza_valor();
}

function atualiza_valor(){
    visor.innerText = expressao;
}

function calcular(e){
    res = eval(expressao)
    expressao = res
    atualiza_valor()
}