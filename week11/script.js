// --- Color Changer ---
const colorBtn = document.getElementById("colorBtn");

const colors = ["#1a1a2e", "#2d4059", "#3a0ca3", "#7209b7", "#f72585", "#4cc9f0"];

colorBtn.addEventListener("click", function () {
    const randomIndex = Math.floor(Math.random() * colors.length);
    document.body.style.backgroundColor = colors[randomIndex];
});

// --- Click Counter ---
const countBtn = document.getElementById("countBtn");
let count = 0;

countBtn.addEventListener("click", function () {
    count++;
    countBtn.textContent = "Click Counter: " + count;
});

// --- Greet User ---
const greetBtn = document.getElementById("greetBtn");
const nameInput = document.getElementById("nameInput");
const output = document.getElementById("output");

greetBtn.addEventListener("click", function () {
    const name = nameInput.value.trim();

    if (name === "") {
        output.textContent = "Please enter your name!";
    } else {
        output.textContent = "Hello, " + name + "! Welcome to Week 11!";
    }
});
