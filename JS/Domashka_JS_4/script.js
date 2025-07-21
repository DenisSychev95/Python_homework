"use strict";
let months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"];

function divColor(){
    let r = Math.floor(Math.random() * 256);
    let g = Math.floor(Math.random() * 256);
    let b = Math.floor(Math.random() * 256);
    let styleColor = `rgb(${r},${g},${b})`
    return styleColor  
}

for(let i = 0; i < months.length; i++){
    document.writeln("<div id='"+ i +"'></div>");
    let id = document.getElementById("" + i);
    id.style.textAlign = "center";
    id.style.height = "50px";
    id.style.fontWeight = "bold";
    id.style.fontSize = "26pt";
    id.style.background = divColor();
    id.innerHTML = months[i];

}