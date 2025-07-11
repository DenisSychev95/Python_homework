"use strict";

let s_r1 = "Стоимость покупки без скидки: ";
let s_r2 = "Скидка: ";
let s_r3 = "Итоговая стоимость: ";
let currency = "руб";
let discount = "отсутствует";
let discount1 = 5;
let discount2 = 3;
let summ = prompt("Введите стоимость покупки: ");
let row1 = s_r1 + summ + currency;
let row2, row3;

// if (summ > 1000){
//     row2 = s_r2 + discount1 + "%";
//     row3 = s_r3 + (0.01*(100-discount1)*summ).toFixed(2) + currency;
//     alert(`${row1}
// ${row2}
// ${row3}`);
// }
// else if (summ > 500 && summ < 1000){
//     row2 = s_r2 + discount2 + "%";
//     row3 = s_r3 + (0.01*(100-discount2)*summ).toFixed(2) + currency;
//     alert(`${row1};
// ${row2}
// ${row3}`);
// }
// else{
//     row2 = s_r2 + discount;
//     row3 = s_r3 + summ + currency;
//     alert(row1 + "\n" + row2 + "\n"+row3);
// };

// if (summ > 1000){
//     row2 = s_r2 + discount1 + "%";
//     row3 = s_r3 + (0.01*(100-discount1)*summ).toFixed(2) + currency;
//     alert(`${row1}
// ${row2}
// ${row3}`);
// }
// if (summ > 500 && summ < 1000){
//     row2 = s_r2 + discount2 + "%";
//     row3 = s_r3 + (0.01*(100-discount2)*summ).toFixed(2) + currency;
//     alert(`${row1};
// ${row2}
// ${row3}`);
// }
// if(summ <= 500){
//     row2 = s_r2 + discount;
//     row3 = s_r3 + summ + currency;
//     alert(row1 + "\n" + row2 + "\n"+row3);
// };

let res1 = row1 + "\n"+ s_r2 + discount1 + "%" +"\n" + s_r3 + (0.01*(100-discount1)*summ).toFixed(2) + currency;
let res2 = row1 + "\n" + s_r2 + discount2 + "%" + "\n" + s_r3 + (0.01*(100-discount2)*summ).toFixed(2) + currency;
let res3 = row1 + "\n" + s_r2 + discount + "\n" + s_r3 + summ + currency;
summ <= 500 ? alert(res3) : summ < 1001 ? alert(res2) : alert(res1);