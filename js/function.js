// function greet(name, greetings) {
//     return `${greetings}, ${name}! `;
// }

// console.log(greet("Eris", "Welcome"));

// const greeting = (name, greeting) => `${greeting}, ${name}!`; //arrow function

// console.log(greeting("Eris", "Welcome"));

const students = ["Eric", "Beatriz", "Hanna"];
const marks = [20, 75, 50];
const dept = ["IT", "CS", "ECE"];

function ranks(mark) {
    if (mark < 40) {
        return "F";
    } else {
        return "P";
    }
}

for (let i = 0; i < students.length; i++) {
    console.log("Name:", students[i]);
    console.log("Mark:", marks[i]);
    console.log("Dept:", dept[i]);
    console.log("Ranks:", ranks(marks[i]));
    console.log();
}
let j = 0;
let count_p = 0;
let count_f = 0;
while (j < students.length) {
    if (ranks(marks[j]) === "P") {
        count_p++;
    } else {
        count_f++;
    }
    j++;
}

console.log("Number of students passed:", count_p);
console.log("Number of studnets failed:", count_f);
