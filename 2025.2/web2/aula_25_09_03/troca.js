function minha_funcao(e) {
    var imagem = document.querySelector("#img");
    nome_imagem = imagem.getAttribute("src");
    if(nome_imagem == "img/volvo.jpg"){
        imagem.setAttribute("src", "img/saladeaula.jpg");
    } else {
        imagem.setAttribute("src", "img/volvo.jpg");
    }

}