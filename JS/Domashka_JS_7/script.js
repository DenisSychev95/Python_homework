"use strict";

let btnS = document.querySelectorAll(".remove-button");

for (let i = 0; i < btnS.length; i++) {
    btnS[i].addEventListener("click", () => {
        btnS[i].parentNode.remove();
    });

};



