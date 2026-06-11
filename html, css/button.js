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
