function printOutput(data) {
    document.getElementById("output").innerHTML = data;
}

function greet() {
    let name = document.getElementById("input").value;

    if (name === "") {
        printOutput(null);
    } else {
        result = "Welcome " + name + "!";
        printOutput(result);
    }
}

let fruits = ["Apple", "Banana", "Cucumber"];
function loop() {
    let result = "";
    for (let i = 0; i < fruits.length; i++) {
        result += fruits[i] + "<br>";
    }
    printOutput(result);
}

function clear1() {
    document.getElementById("output").innerHTML = "";
}

function change_color() {
    document.getElementById("title").style.color = "blue";
}

const students = ["Eric", "Beatriz", "Hanna"];
let index = 0;
function character() {
    const stud_len = [];

    for (let i = 0; i < students.length; i++) {
        let count = 0;
        for (const letter of students[i]) {
            count++;
        }
        stud_len.push(count);
    }

    if (index < students.length) {
        result = students[index] + " " + stud_len[index];
        printOutput(result);
        index++;
    } else {
        printOutput("No more students");
    }
}
