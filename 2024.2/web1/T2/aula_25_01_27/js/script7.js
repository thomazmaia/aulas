function somar(){
    let val1 = parseInt(document.getElementById("v1").value);
    let val2 = parseInt(document.getElementById("v2").value);
    let res = val1 + val2;
    document.getElementById("resultado").textContent = "Resultado: " + res;
}

function subtrair(){
    let val1 = parseInt(document.getElementById("v1").value);
    let val2 = parseInt(document.getElementById("v2").value);
    let res = val1 - val2;
    document.getElementById("resultado").textContent = "Resultado: " + res;
}