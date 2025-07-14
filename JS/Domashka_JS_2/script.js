"use strict";

// Простое решение

// document.writeln("<table border='1' width='400'>");
// for(let a = 1; a < 11; a++){
//     document.writeln("<tr align='center'>")
//     for(let b = 1; b < 11; b++){
//         if(a%2){if(b%2){
//               document.writeln("<td bgcolor='red'>" + a*b + "</td>")  
//             }
//             else{document.writeln("<td bgcolor='yellow'>" + a*b + "</td>")}


//         }
//         else{            if(b%2){
//               document.writeln("<td bgcolor='yellow'>" + a*b + "</td>")  
//             }
//             else{document.writeln("<td bgcolor='red'>" + a*b + "</td>")}



//         }
//     }
//     document.writeln("</tr>")
// }
// document.writeln("</table>");

// Усложненный вариант
document.writeln("<table border='1' width='400'>");
for (let a = 0; a < 11; a++) {
    document.writeln("<tr align='center'>")
    for (let b = 0; b < 11; b++) {
        if (a == 0) {
            document.writeln("<td >" + b + "</td>")
        }
        else {
            if (b == 0) {
                document.writeln("<td >" + a + "</td>")
            }
            else {
                if (a % 2) {
                    if (b % 2) {
                        document.writeln("<td bgcolor='red'>" + a * b + "</td>")
                    }
                    else { document.writeln("<td bgcolor='yellow'>" + a * b + "</td>") }


                }
                else {
                    if (b % 2) {
                        document.writeln("<td bgcolor='yellow'>" + a * b + "</td>")
                    }
                    else { document.writeln("<td bgcolor='red'>" + a * b + "</td>") }



                }
            }

        }
    }
    document.writeln("</tr>")
}
document.writeln("</table>");
