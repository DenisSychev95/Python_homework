/* let start = document.querySelector("#start");
let game = document.querySelector("#game");
let score = 0;
let time = document.querySelector("#time");
let isGameStarted = false;

// мое дописано получили доступ к input nunmber
let settings = document.querySelector("#game-time");
let result = document.querySelector("#result");
//


start.addEventListener("click", startGame);

game.addEventListener("click", handleBoxClick);

function startGame() {
    isGameStarted = true;
    start.classList.add("hide");

    //мое дописано
    letToggle("result-header", "time-header");
    score = 0;
    //


    game.style.background = "#FFF";

    let interval = setInterval(function () {
        let t = time.textContent;

        if (t <= 0) {
            clearInterval(interval);
            endGame();

        }
        else {
            time.textContent = (t - 0.1).toFixed(1);
        }
    }, 100)
    renderBox();


}
function renderBox() {
    game.innerHTML = "";
    let box = document.createElement("div");
    let boxSize = getRandon(30, 100);

    let gameSize = game.getBoundingClientRect();
    let maxTop = gameSize.height - boxSize;
    let maxLeft = gameSize.width - boxSize;


    box.style.width = box.style.height = `${boxSize}px`;

    //box.style.background = "#000";
    // мое дописано цвет квадрата
    box.style.background = randColor();
    //
    box.style.position = "absolute";
    box.style.top = `${getRandon(0, maxTop)}px`;
    box.style.left = `${getRandon(0, maxLeft)}px`;
    box.style.cursor = "pointer";
    box.setAttribute("data-box", "true");

    game.insertAdjacentElement("afterbegin", box);
}

function handleBoxClick(event) {
    if (!isGameStarted) {
        return;
    }
    if (event.target.dataset.box) {
        score++;
        renderBox();

    }

}

function getRandon(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
}

function endGame() {
    isGameStarted = false;
    game.innerHTML = "";
    start.classList.remove("hide");
    game.style.background = "#9be8fb";

    // мое дописано установили время из инпута
    //time.textContent = settings.value;
    //document.querySelector("#time-header").classList.add("hide");
    //document.querySelector("#result-header").classList.remove("hide");
    letToggle("time-header", "result-header");
    time.textContent = `${settings.value}.0`;
    result.textContent = score;
    //

}

//мое дописано
function randColor() {
    return `rgb(${Math.floor(Math.random() * 256)},${Math.floor(Math.random() * 256)},${Math.floor(Math.random() * 256)})`
}
//
//мое дописано
function letToggle(id1, id2) {
    document.querySelector(`#${id1}`).classList.add("hide");
    document.querySelector(`#${id2}`).classList.remove("hide");
}
// */

let start = document.querySelector("#start");
let game = document.querySelector("#game");
let time = document.querySelector("#time");
let timeHeader = document.querySelector("#time-header");
let resultHeader = document.querySelector("#result-header");
let result = document.querySelector("#result");
let gameTime = document.querySelector("#game-time");

let score = 0;
let isGameStarted = false;

start.addEventListener("click", startGame);
game.addEventListener("click", handleBoxClick);
gameTime.addEventListener("input", setGameTime);

function startGame() {
    score = 0;

    setGameTime();
    gameTime.setAttribute("disabled", "true");
    timeHeader.classList.remove("hide");
    resultHeader.classList.add("hide");

    isGameStarted = true;
    //
    /* gameTime.removeEventListener("input", setGameTime); */
    //
    start.classList.add('hide');
    game.style.background = "#FFF";

    let interval = setInterval(function () {
        let t = time.textContent;
        if (t <= 0) {
            clearInterval(interval);
            endGame();
        } else {
            time.textContent = (t - 0.1).toFixed(1);
        }
    }, 100);

    renderBox();
}

function endGame() {
    isGameStarted = false;
    game.innerHTML = "";
    result.textContent = score;
    gameTime.removeAttribute("disabled");
    start.classList.remove('hide');
    game.style.background = "#9be8fb";
    timeHeader.classList.add("hide");
    resultHeader.classList.remove("hide");
    

}

function getRandom(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
}

function renderBox() {
    game.innerHTML = "";
    let box = document.createElement("div");
    let boxSize = getRandom(30, 100);

    let gameSize = game.getBoundingClientRect();
    let maxTop = gameSize.height - boxSize;
    let maxLeft = gameSize.width - boxSize;

    box.style.width = box.style.height = boxSize + "px";
    box.style.background = randColor();
    box.style.position = "absolute";
    box.style.top = getRandom(0, maxTop) + "px";
    box.style.left = getRandom(0, maxLeft) + "px";
    box.style.cursor = "pointer";
    box.setAttribute("data-box", 'true');

    game.insertAdjacentElement("afterbegin", box);
}

function handleBoxClick(event) {
    if (!isGameStarted) {
        return;
    }
    if (event.target.dataset.box) {
        score++;
        renderBox();
    }
}

function setGameTime() {
    let tm = +gameTime.value;
    time.textContent = tm.toFixed(1);
    timeHeader.classList.remove("hide");
    resultHeader.classList.add("hide");
}

function randColor() {
    return `rgb(${Math.floor(Math.random() * 256)},${Math.floor(Math.random() * 256)},${Math.floor(Math.random() * 256)})`
}