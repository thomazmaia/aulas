const btn = document.getElementById("btn");

// btn.addEventListener("click", function minha_funcao() { 
//     document.body.style.background = "red"; 
// });

btn.addEventListener("click", () => { 
    document.body.style.background = "red"; 
});


btn.addEventListener("mousemove", () => { 
    document.body.style.background = "blue"; 
});
