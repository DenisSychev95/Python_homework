"use strict";

// Доступ к кнопке button
let button = document.querySelector("button");

// Доступ к форме
let myForm = document.form1;


//Доступ к input(name,phone), div(errorName,errorPhone )

let userName = document.querySelector("#name");
let userPhone = myForm.phone;
let errorName = document.querySelector("#errorName");
let errorPhone = document.querySelector("#errorPhone");

// Шаблон для поля имени
let regName = /^[a-zа-яё'-]{1,15}[_'\s-]?[a-zа-яё'-]{1,15}[_'\s-]?[a-zа-яё'-]{1,15}$/i;

// Шаблон для поля телефона- мобильный или городской(без кода города)
let regPhone = /^(([\s]*[+-]?[78][\s-]?9[0-9]{2}[\s-]?[0-9]{3}[\s-]?[0-9]{2}[\s-]?[0-9]{2})|(\s*\d{2,3}[\s-]?\d{2}[\s-]?\d{1,2}))$/;

//Функция применения стилей к input
function checkInput(inputName, reg, tagError) {
    let value = inputName.value;
    if (reg.test(value)) {
        inputName.style.border = "3px solid green";
        tagError.style.visibility = "hidden";
        return true;


    }
    else {
        inputName.style.border = "3px solid red";
        tagError.style.visibility = "visible";
        return false;

    }
};

function formClear(tagName, errorName) {
    tagName.style.border = "1px solid black";
    errorName.style.visibility = "hidden";

};

function validation(inputName, reg) {
    let value = inputName.value;
    if (reg.test(value)) {
        return true;
    }
    else {
        return false;
    }
}

//События ввода в поля input(name, phone)

userName.addEventListener("input", () => checkInput(userName, regName, errorName));
userPhone.addEventListener("input", () => checkInput(userPhone, regPhone, errorPhone));







//Флаг isSending- блокирует повторную отправку формы
let isSending = false;
// Событие клика по кнопке

myForm.addEventListener("submit", function (event) {
    event.preventDefault();
    // Проверка валидации содержимого
    let validName = validation(userName, regName);
    let validPhone = validation(userPhone, regPhone);


    if (!validName || !validPhone) {
        let err = document.createElement("div");
        err.classList.add("object");
        err.innerHTML = "<img src='fail1.png' alt=''><p>Ошибка! Пожалуйста заполните поля формы корректно.</p><input type='button' value='Ок' id='btn'>";
        document.body.appendChild(err);

        let btn = document.querySelector("#btn")
        btn.style.width = "70px";
        btn.style.marginTop = "5px";
        err.style.height = "130px";
        err.style.width = "220px";
        err.style.padding = "5px";
        btn.addEventListener("click", () => {
            err.remove();
            isSending = false;
            button.disabled = false;
        });


        return;
    }

    if (isSending) {
        return;
    }



    let formData1 = new FormData(myForm);
    let userText = userName.value;

    isSending = true;
    button.disabled = true;
    let myPromise = new Promise(function (resolve, reject) {
        let intro = document.createElement("div");
        intro.classList.add("object");
        intro.innerHTML = "<p>Обрабатываю данные пользователя... <img src='Sandclock.gif' alt=''></p>";
        document.body.appendChild(intro);
        resolve(intro)
    })
        .then(function (intro) {
            return new Promise(function (resolve, reject) {
                setTimeout(() => {
                    intro.remove();
                    myForm.reset();
                    formClear(userName, errorName);
                    formClear(userPhone, errorPhone);
                    resolve();
                }, 4000)
            })
        })
        .then(function () {
            return new Promise(function (resolve, reject) {
                let outro = document.createElement("div");
                outro.classList.add("object");
                outro.innerHTML = "<p>Данные успешно обработаны! <img src='1.png' alt=''></p><input type='button' value='Ок' id='btn'>";
                document.body.appendChild(outro);
                let btn = document.querySelector("#btn")
                btn.style.width = "70px";
                btn.style.marginTop = "5px";
                outro.style.height = "100px";
                btn.addEventListener("click", () => {
                    outro.remove();
                    /*                     isSending = false;
                            ;            button.disabled = false; */
                    resolve();
                })

            })

        })
        .then(function () {
            return new Promise(function (resolve, reject) {
                let message = document.createElement("div");
                message.classList.add("object");
                message.innerHTML = "<p>Загружаю данные на сервер...<img src='load.gif' alt=''></p>";
                document.body.appendChild(message);

                setTimeout(function () {
                    message.remove();
                    resolve();
                }, 3000)

            })

        })
        .then(function () {
            return new Promise(function (resolve, reject) {
                let outro = document.createElement("div");
                outro.classList.add("object");
                outro.innerHTML = `<p>${userText}, ваши данные успешно сохранены в Базу Данных! </p><img src='fine.png' alt=''><br><input type='button' value='Завершить работу' id='btn'>`;
                document.body.appendChild(outro);
                let btn = document.querySelector("#btn")
                btn.style.width = "150px";
                btn.style.marginTop = "5px";
                outro.style.height = "130px";
                outro.style.width = "230px";
                outro.style.left = "40px"
                btn.addEventListener("click", () => {
                    outro.remove();
                    isSending = false;
                    button.disabled = false;

                    resolve();
                })
            })
        })

});

/*                     isSending = false;
        ;            button.disabled = false; *//*         .then(function(){
return new Promise(function(resolve,reject){
let request = new XMLHttpRequest();
request.open("POST", "server.php");
request.send(formData1);
request.addEventListener("load", function(){
if(request.status == 200){
let outro = document.createElement("div");
outro.classList.add("object");
outro.innerHTML = "<p>Данные загружены на сервер! <img src='fine.png' alt=''></p><input type='button' value='Завершить работу' id='btn'>";
document.body.appendChild(outro);
let btn = document.querySelector("#btn")
btn.style.width = "70px";
btn.style.marginTop = "5px";
outro.style.height = "100px";
btn.addEventListener("click", () => {
outro.remove();

resolve();
})
}
else{
 
}
})
})
}) */