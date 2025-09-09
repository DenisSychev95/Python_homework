"use strict";

let rub = document.querySelector("#rub");
let usd = document.querySelector("#usd");
let eur = document.querySelector("#eur");

rub.addEventListener("input", ()=>{
    let request = new XMLHttpRequest();
    request.open("GET", "homework.json");
    request.setRequestHeader("Content-type", "application/json; charset=utf-8");
    request.send();

    request.addEventListener("load", ()=>{
        if(request.status == 200){
            let finance = JSON.parse(request.response);
            console.log(finance);
        
            usd.value = (rub.value / finance.currency.usd).toFixed(2);
            eur.value = (rub.value / finance.currency.eur).toFixed(2);
    }
        else{
            usd.value = "Ошибочка.Конвертер не загрузился =(";
            eur.value = "Ошибочка.Конвертер не загрузился =(";
    }
});
})

