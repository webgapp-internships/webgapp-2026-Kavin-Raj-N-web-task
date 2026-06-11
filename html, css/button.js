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
    let result2 = "";
    for (let i = 0; i < fruits.length; i++) {
        result2 += fruits[i] + "<br>";
    }
    printOutput(result2);
}
