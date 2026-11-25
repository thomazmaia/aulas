let caixa = document.getElementById("caixa");

function mudar_cor(e){
    let cor = caixa.style.backgroundColor;

    if (cor == "blue") {
        caixa.style.backgroundColor = "red";
    } else {
        caixa.style.backgroundColor = "blue";
    }
}