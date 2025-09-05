"use strict";

let dict = {
    zero: {
        id: "zero",
        img: "https://cdn0.iconfinder.com/data/icons/contact-us-set-1-8/64/Contact_us_1-09-64.png",
        text: "Работа 24 часа в сутки, 7 дней в неделю, 365 дней в году"
    },
    one: {
        id: "one",
        img: "https://cdn3.iconfinder.com/data/icons/unigrid-phantom-science-vol-1/60/003_042_planet_earth_globe_world_worldwide_space_cosmos_science_solar_system-64.png",
        text: "Нет географических границ"
    },
    two: {
        id: "two",
        img: "https://cdn0.iconfinder.com/data/icons/business-set-2-6/512/8-64.png",
        text: "Ассортимент"
    },
    three: {
        id: "three",
        img: "https://cdn2.iconfinder.com/data/icons/medicine-and-medical-diagnostics-1/32/Medicine_health_and_safety_care_health_insurance-64.png",
        text: "Безопасность"
    },
    four: {
        id: "four",
        img: "https://cdn3.iconfinder.com/data/icons/robots-flat-collection/60/Robots_-_Flat_-_007_-_Robocop-64.png",
        text: "Сокращение расходов на аренду и персонал"
    },
    five: {
        id: "five",
        img: "https://cdn2.iconfinder.com/data/icons/stock-market-10/512/partner-partnership-people-business-hand-stock-market-shake-64.png",
        text: "Партнерские отношения"
    },
    six: {
        id: "six",
        img: "https://cdn2.iconfinder.com/data/icons/smart-technology-part-1/64/on-demand-service-64.png",
        text: "Покупатель всегда на связи"
    },
    seven: {
        id: "seven",
        img: "https://cdn3.iconfinder.com/data/icons/work-life-balance-and-stress-management-flat/64/happiness-smile-pleasure-delight-positive-comfortable-enjoyable-64.png",
        text: "Комфортный выбор"
    },
    eight: {
        id: "eight",
        img: "https://cdn2.iconfinder.com/data/icons/popicon-part-1/256/01-64.png",
        text: "Удобство оплаты"
    }
};

let container = document.querySelector("#container");
container.style.cssText = `
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;

`;


class Element {
    constructor(object) {
        this.params = object;
    };

    createElem() {
        let { id, img, text } = this.params
        let myCSS = `
            width: 280px;
            height: 170px;
            box-sizing: border-box;
            box-shadow: 0 0 5px 5px gray;
            margin-bottom: 20px;
            margin-left: 20px;
            text-align: center;
            padding: 20px;
            font-size: 16px;
            font-weight: bold; 
        `;
        container.insertAdjacentHTML("beforeend", `<div id='${id}' style='${myCSS}'><img src='${img}' alt=''><p>${text}</p></div>`);

    };
};

let elem0 = new Element(dict.zero);
let elem1 = new Element(dict.one);
let elem2 = new Element(dict.two);
let elem3 = new Element(dict.three);
let elem4 = new Element(dict.four);
let elem5 = new Element(dict.five);
let elem6 = new Element(dict.six);
let elem7 = new Element(dict.seven);
let elem8 = new Element(dict.eight);

let myArray = [elem0, elem1, elem2, elem3, elem4, elem5, elem6, elem7, elem8];

for (let i = 0; i < myArray.length; i++) {
    myArray[i].createElem();
};