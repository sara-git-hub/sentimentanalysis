const form = document.getElementById("sentiment-form");
const resultBox = document.getElementById("result-box");
const resultText = document.getElementById("result-text");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const text = document.getElementById("text-input").value;

    const response = await fetch("/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text })
    });

    const data = await response.json();

    resultText.textContent = JSON.stringify(data, null, 4);
    resultBox.style.display = "block";
});
