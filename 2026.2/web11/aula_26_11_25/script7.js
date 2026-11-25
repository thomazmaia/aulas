let imagem = document.querySelector("#imagem");

function aumentar(e){
    let largura = parseInt(imagem.getAttribute("width"));
    largura = largura + 50;
    imagem.setAttribute("width", largura);
}


function mudar_imagem(e) {
    let path = imagem.getAttribute("src");

    if (path == "img/relampago.jpg") {
        imagem.setAttribute("src", "img/homemdeferro.jpg");
    } else {
        imagem.setAttribute("src", "img/relampago.jpg");
    }
}