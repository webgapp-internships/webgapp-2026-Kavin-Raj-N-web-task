// const a = "hello";
// if (a == "hi") {
//     console.log(a);
// } else {
//     console.log("enter valid string");
// }

// const a = 50;
// const b = 40;
// let c = a + b;
// if (c >= 90) {
//     console.log("Grade A");
// } else if (c >= 80) {
//     console.log("Grade B");
// } else if (c >= 70) {
//     console.log("Grade C");
// } else {
//     console.log("Grade D");
// }

// const fruits = ["apple", "banana", "cucumber"];
// for (let i = 0; i < fruits.length; i++) {
//     let count = 0;
//     for (const letter of fruits[i]) {
//         count++;
//     }
//     console.log(fruits[i], count);
// }

const students = ["Eric", "Beatriz", "Hanna"];

let i = 0;

while (i < students.length) {
    let count = 0;
    let j = 0;

    while (j < students[i].length) {
        count++;
        j++;
    }

    console.log(students[i], count);
    i++;
}
