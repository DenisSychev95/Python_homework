"use strict";
let button = document.querySelector("#btn");
let complete = document.querySelector("#complete");
let url = "https://jsonplaceholder.typicode.com/todos";

button.addEventListener("click", showUsers);

async function showUsers() {
    let response = await fetch(url);
    let dataObject = await response.json();

    let showData = dataObject.map(function (item) {
        if(item.completed){
        let li = `<li>Пользователь: ${item.userId} выполнил задачу № ${item.id} (${item.title})</li><br>`
        return li;}
    })
    document.querySelector("#array").insertAdjacentHTML("afterbegin", showData.join(" "));
    button.remove();
    complete.innerHTML = "<h2>Задание выполнено!</h2>";
    complete.style.textAlign = "center";
    complete.style.position = "sticky";
    complete.style.top = "0px";
}

