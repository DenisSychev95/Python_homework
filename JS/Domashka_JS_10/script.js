"use strict";

function Person(name, age, job) {
    this.name = name;
    this.age = age;
    this.job = job;
    this.who = function () {
        document.writeln(`<p>Я <b>${this.name}</b> мне <b>${this.age}</b> лет. Я работаю <b>${this.job}ом</b>.</p>`)
    };

};

let employee1 = new Person("Дмитрий", 26, "Дизайнер");
let employee2 = new Person("Станислав", 29, "Программист");
let employee3 = new Person("Сергей", 35, "Менеджер");

let arr = [employee1, employee2, employee3];
for (let i = 0; i < arr.length; i++) {
    arr[i].who();
    
}