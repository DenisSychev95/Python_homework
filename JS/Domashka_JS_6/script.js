"use strict";

container.style.cssText = `
    width: 800px;
    height: 400px;
    border: 2px solid gray;
    padding: 40px;
    box-sizing: border-box;

`
content.style.display = "flex";
content.style.flexDirection = "row";
content.style.flexWrap = "wrap";
content.style.justifyContent = "space-around";
content.style.height = "140px"

let div = document.querySelectorAll(".inner");
for (let i = 0; i < div.length; i++) {
    div[i].style.cssText = `
        width: 170px;
        height: 130px;
        padding: 5px;
        border: 1px solid;
        box-sizing: border-box;
    `
    let a = i + 2;
    div[i].innerHTML = `<img src='${i + 2}.jpg' alt=''>`
}


fields1.style.cssText = `
    font-weight: bold;
    font-size: 20px;
    margin: 40px auto;
    text-align: center;
`
butt.style.cssText = `
    display : block;
    margin : 40px auto;
    font-weight : bold;
    font-size : 30px;
    cursor : pointer;
    width : 250px;
`
let inp = document.querySelectorAll("input");
for(let e = 0; e < inp.length - 1 ; e++){
    inp[e].style.width = "35px" 
}

let left, right, ind1, ind2;

let images = document.querySelectorAll("img");


butt.addEventListener("click", changeImg);

function cleaner(){
    for(let d = 0; d < inp.length - 1 ; d++){
    inp[d].value = ""; 
}
};

function changeImg() {
    left = inp[0].value;
    right = inp[1].value;
    ind1 = left - 1;
    ind2 = right - 1;

    if ((1 <= left && left <= 3) && (1 <= right && right <= 3)) {
        if (left != right) {
            
            let a = images[ind1].src
            let b = images[ind2].src
            images[ind1].src = b;
            images[ind2].src = a;

            console.log(a,b);
            
        }
        else {
            alert("Ничего не произошло")
            cleaner()
        }
    }
    else {
        alert("Некорректное значение")
        cleaner()
    }
}


