async function indexWebsite() {

    const url =
        document.getElementById("url").value;

    document.getElementById("status")
        .innerText = "Indexing website...";

    const response = await fetch(
        "/index",
        {
            method: "POST",
            headers: {
                "Content-Type":
                    "application/json"
            },
            body: JSON.stringify({
                url: url
            })
        }
    );

    const data = await response.json();

    document.getElementById("status")
        .innerText = data.message;
}


async function askQuestion() {

    const question =
        document.getElementById("question").value;

    document.getElementById("answer")
        .innerText = "Thinking...";

    const response = await fetch(
        "/ask",
        {
            method: "POST",
            headers: {
                "Content-Type":
                    "application/json"
            },
            body: JSON.stringify({
                question: question
            })
        }
    );

    const data = await response.json();

    document.getElementById("answer")
        .innerText = data.answer;
}