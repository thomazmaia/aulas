var primeiraCarta = null;

function virar1(){
    let carta = document.querySelector("#carta1");
    carta.setAttribute("src", "A.png");
    checar("A");
}

function virar2(){
    let carta = document.querySelector("#carta2");
    carta.setAttribute("src", "B.png");
    checar("B");
}

function virar3(){
    let carta = document.querySelector("#carta3");
    carta.setAttribute("src", "B.png");
    checar("B");
}

function virar4(){
    let carta = document.querySelector("#carta4");
    carta.setAttribute("src", "A.png");
    checar("A");
}

function checar(valor){
    if (primeiraCarta == null) {
        primeiraCarta = valor;
    } else {
        if (primeiraCarta == valor) {
            document.querySelector("#status").textContent = "Você acertou";
        } else {
            document.querySelector("#status").textContent = "Você errou";
        }
        primeiraCarta = null;
    }
}

function reiniciar(){
    // document.querySelector("#carta1").setAttribute("src", "verso.png");
    // document.querySelector("#carta2").setAttribute("src", "verso.png");
    // document.querySelector("#carta3").setAttribute("src", "verso.png");
    // document.querySelector("#carta4").setAttribute("src", "verso.png"); 
    for (let i = 1; i <= 4; i++) {
        document.querySelector("#carta" + i).setAttribute("src", "verso.png");
    }
    document.querySelector("#status").textContent = "Status - Clique em alguma imagem";
    primeiraCarta = null;
}