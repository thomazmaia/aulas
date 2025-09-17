function add_img(){
    var local = document.getElementById('container');
    var var_img = document.createElement('img');

    var_img.setAttribute("src", "../aula_25_09_04/A.png")

    local.appendChild(var_img);    
}

function add_texto(){
    var local = document.getElementById('container');
    var var_p = document.createElement('p');

    var_p.textContent = "Fui criado agora...";

    local.appendChild(var_p);
}

function add_lista(){
    var local = document.getElementById('container');
    var_lista = document.createElement('ul');
    local.appendChild(var_lista);
   
    var_item = document.createElement('li');
    var_item.textContent = "Item 1";
    local.appendChild(var_item);
}