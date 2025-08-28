"use strict";
let btn = document.querySelector("input[type='button']");
let userMessage = document.forms.form.message.value
btn.addEventListener("click", addText);

function addText(){
    let hidden = document.querySelector("#hidden"); 
    let content = document.querySelector("#content");
    hidden.style.visibility = "visible";
    //let pattern = /([a-z0-9._-]+@(mail|gmail|bk)\.(com|ru))/gi;
    let pattern = /(\w+[.-]?\w+@(mail|gmail|bk)\.(com|ru))/gi; // более универсальный шаблон
    let printMessage = userMessage.replace(pattern, "<span style='color : red; font-weight: bold;'>$1</span>");
    content.innerHTML = printMessage;
};