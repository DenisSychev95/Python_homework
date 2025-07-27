"use strict";
let userInput = prompt("Как вас зовут?");
let userName;
if(userInput){
    userName = `<span id='userName'>${userInput}</span>`; 
}
else{
    userName = `<span id='userName'>Neo</span>`;
};

let bluestr = `<span id='bluestr'>синюю</span>`;
let redstr = `<span id='redstr'>красную</span>`;
let text1 = `Здравствуй ${userName}, это твой последний шанс. После этого нет пути назад. Ты берешь ${bluestr} таблетку — и сказка кончается, ты просыпаешься в своей постели и веришь, во что хочешь верить. Берешь ${redstr} таблетку — остаешься в стране чудес, и я покажу тебе, насколько глубока кроличья нора.`;

function getId(idName) {
    return document.querySelector("#" + idName);
};

window.addEventListener("load", createBg);

function createBg() {

    // флекс контейнер
    document.body.innerHTML = "<div id='container'><div id='block'></div><div id='image'></div></div>";
    let container = getId("container");
    container.style.display = "flex";
    container.style.flexDirection = "row";
    container.style.flexWrap = "wrap";
    // левый флекс-элемент
    let id = getId("block");
    id.style.width = "800px";
    id.style.height = "0";
    id.style.background = "url('greencode.gif')";
    id.style.position = "relative";
    id.style.transition = "height 5s linear";

    setTimeout(() => id.style.height = "690px", 50);
    setTimeout(changeBg, 5000);
};

function changeBg() {
    let id = getId("block");
    id.style.background = "url('morfeus.jpg')";

    setTimeout(createObject1, 500);
    setTimeout(createObject2, 1000);
    setTimeout(createObject3, 1500);

    // создание левой пилюли
    let ltab = document.createElement("div");
    ltab.id = "ltab";

    ltab.style.width = "43px";
    ltab.style.height = "26px";
    ltab.style.borderRadius = "50%";
    ltab.style.position = "absolute";
    ltab.style.top = "576px";
    ltab.style.left = "126px";
    ltab.style.transform = "rotate(319deg)";
    ltab.style.background = "rgba(255, 255 , 255, 0.01)";

    id.appendChild(ltab);

    // создание правой пилюли
    let rtab = document.createElement("div");
    rtab.id = "rtab";
    rtab.style.cssText = `
        position: absolute;
        width: 43px;
        height: 26px;
        top: 577px;
        left: 632px;
        border-radius: 50%;
        transform: rotate(40deg);
        background: rgba(255, 255 , 255, 0.01);
    `;
    id.appendChild(rtab);
};

// создание первого пузырька
function createObject1() {
    let id = getId("block");
    let circle1 = document.createElement("div");
    circle1.id = "circle1";

    circle1.style.width = "30px";
    circle1.style.height = "20px";
    circle1.style.background = "white";
    circle1.style.borderRadius = "30%";
    circle1.style.position = "absolute";
    circle1.style.top = "165px";
    circle1.style.left = "425px";

    id.appendChild(circle1);
};

// создание второго пузырька
function createObject2() {
    let id = getId("block");
    let circle2 = document.createElement("div");
    circle2.id = "circle2";

    circle2.style.width = "55px";
    circle2.style.height = "35px";
    circle2.style.background = "white";
    circle2.style.borderRadius = "30%";
    circle2.style.position = "absolute";
    circle2.style.top = "140px";
    circle2.style.left = "454px";

    id.appendChild(circle2);
};

// создание третьего пузырька
function createObject3() {
    let id = getId("block");
    let bubble = document.createElement("div");
    bubble.id = "bubble";

    bubble.style.width = "250px";
    bubble.style.height = "150px";
    bubble.style.background = "white";
    bubble.style.borderRadius = "20%";
    bubble.style.position = "absolute";
    bubble.style.top = "10px";
    bubble.style.left = "509px";
    bubble.style.overflow = "auto";
    bubble.style.textAlign = "center";
    bubble.style.padding = "9px 12px";
    id.appendChild(bubble);

    let i = 0;
        animText();
        // анимированный текст внутри третьего пузырька
        function animText(){
            bubble.innerHTML = text1.slice(0,i);
            i++;
            let bluestrId =getId("bluestr");
            
            let userName = getId("userName");
            if(userName){
                userName.style.fontWeight="bold";
                userName.style.fontSize="18px";
            };

            if(bluestrId){
            
            bluestrId.style.color = "blue";
            bluestrId.style.fontWeight = "bold";
            bluestrId.style.textDecoration = "underline";
        };
            let redstrId =getId("redstr");
            if(redstrId){
            
            redstrId.style.color = "red";
            redstrId.style.fontWeight = "bold";
            redstrId.style.textDecoration = "underline";
        };

            if(i > text1.length){
                redstrId.style.cursor = "pointer";
                bluestrId.style.cursor = "pointer";
                //события для красного текста;
                redstrId.addEventListener("mouseover", function(){
                    let red = getId("ltab");
                    red.style.boxShadow = "0 0 8px 10px red";
                });
                redstrId.addEventListener("mouseout", function(){
                    let red = getId("ltab");
                    red.style.boxShadow = "none";
                });
                //события для синего текста;
                bluestrId.addEventListener("mouseover", function(){
                    let blue = getId("rtab");
                    blue.style.boxShadow = "0 0 8px 10px blue";
                });
                bluestrId.addEventListener("mouseout", function(){
                    let blue = getId("rtab");
                    blue.style.boxShadow = "none";
                });
                //события для левой пилюли
                let ltab = getId("ltab");
                ltab.addEventListener("mouseover", function (event) {
                    event.target.style.boxShadow = "0 0 8px 10px red";
                    event.target.style.cursor = "pointer";
                });
                ltab.addEventListener("mouseout", function (event) {
                    event.target.style.boxShadow = "none";
                });
                    //события для правой пилюли
                let rtab = getId("rtab");
                rtab.addEventListener("mouseover", function (event) {
                    event.target.style.boxShadow = "0 0 8px 10px blue";
                    event.target.style.cursor = "pointer";
                });
                rtab.addEventListener("mouseout", function (event) {
                    event.target.style.boxShadow = "none";
                });
                //события для  изображения
                let image = getId("image");
                ltab.addEventListener("click", function(){
                    image.style.height = "0px";
                    image.style.width = "800px";
                    image.style.background = "url('event.jpg')";
                    image.style.transition="height 6s linear";
                    setTimeout(() => image.style.height = "964px", 50);          
                });
                rtab.addEventListener("click", function(){
                    image.style.transition="height 6s linear";
                    setTimeout(() => image.style.height = "0", 50);          
                });

                
                return;
            }
            setTimeout(animText, 30);
        };
};
