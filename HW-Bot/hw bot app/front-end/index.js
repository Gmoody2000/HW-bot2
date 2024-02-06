function submitQuestion() {
    // Get user input
    const userQuestion = document.getElementById('questionInput').value;

    // Simulate bot response (replace this with actual AI logic)
    const botResponse = generateBotResponse(userQuestion);

    // Display bot response
    document.getElementById('botResponse').innerText = botResponse;
}

function generateBotResponse(question) {
    // Add your AI logic here to generate a response based on the user's question
    // For now, let's just echo the question as a simple example
    return `You asked: ${question}`;
}
