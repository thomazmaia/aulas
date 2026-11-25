let imagem = document.getElementById("image");

console.log(imagem.getAttribute("src"));

function mudar_img(e){
    let caminho = imagem.getAttribute("src");
    if (caminho ==  "img/carro.jpg") {
        imagem.setAttribute("src", "img/trem.jpeg");
    } else {
        imagem.setAttribute("src", "img/carro.jpg");
    }   
}

function dar_zoom(e){
    let larg = parseInt(imagem.getAttribute("width"));

    imagem.setAttribute("width", larg * 2)
}