"use strict";
document.writeln("<div id ='JavaScript'></div>");
let text = `Термостат — прибор для поддержания постоянной температуры. Поддержание температуры 
обеспечивается либо за счёт использования терморегуляторов, либо осуществлением фазового 
перехода (например, таяние льда). Для уменьшения потерь тепла или холода термостаты, как 
правило, теплоизолируют. Но не всегда. Широко известны автомобильные моторы, где летом нет 
никакой теплоизоляции и за счёт действия восковых термостатов поддерживается постоянная 
температура. Другим примером термостата, широко используемого в быту, является холодильник.`;
let div = document.querySelector("#JavaScript");
div.innerHTML = text;
div.style.backgroundColor = "yellow";
div.style.color = "black";
div.style.width = "256px";
div.style.height = "256px";
div.style.overflow = "scroll";
div.style.outline = "1px dashed red";

div.className = "resetFont"
let reset = document.querySelector(".resetFont");
reset.style.fontSize = "20pt";
reset.style.fontWeight = "400";
reset.style.textDecoration = "underline"; 

