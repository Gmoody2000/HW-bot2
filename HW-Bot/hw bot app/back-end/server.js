const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const PORT = 3000; // You can choose any available port

// Middleware
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// Simple in-memory storage
let questions = [];

// Routes
app.get('/', (req, res) => {
    res.send('Welcome to the Homework Bot API');
});

// Route to handle user submissions
app.post('/submit-question', (req, res) => {
    const userQuestion = req.body.question;

    // Store the question in memory
    questions.push(userQuestion);

    res.json({ message: 'Question submitted successfully' });
});

// Route to retrieve stored questions
app.get('/get-questions', (req, res) => {
    res.json({ questions });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
