const button1 = document.createElement("button");
button1.className = "button1";
button1.innerText = "Change color";
button1.addEventListener("click", function() {
    if (document.body.style.backgroundColor === "red") {
        document.body.style.backgroundColor = "white";
    } else {
        document.body.style.backgroundColor = "red";
    }     
});
document.body.prepend(button1);
