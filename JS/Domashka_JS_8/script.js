"use strict";


let show = document.querySelector("#show");
let answer = document.form.question;
let btn = document.querySelector("input[type='button']");
let num = Math.floor(Math.random()*5);
answer[num].checked = true;
btn.addEventListener("click", showAnswer);

function showAnswer() {
    show.innerHTML = answer.value;
    show.style.padding = "0 25px";

};

document.querySelector("button[type='button']").addEventListener("click", function () {
    show.innerHTML = "";
})