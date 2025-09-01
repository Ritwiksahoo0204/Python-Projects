let questions = [];
let currentQuestionIndex = 0;
let score = 0;

async function fetchQuestions() {
    const res = await fetch('/api/questions');
    questions = await res.json();
    showQuestion();
}

function showQuestion() {
    if (currentQuestionIndex < questions.length) {
        document.getElementById('question-text').textContent = 
            questions[currentQuestionIndex].text;
        document.getElementById('feedback').textContent = "";
    } else {
        // Quiz completed
        document.getElementById('question-text').textContent = 
            "🎉 Quiz Completed!";
        document.getElementById('feedback').textContent = "";
        document.getElementById('score').textContent = 
            `Final Score: ${score}/${questions.length}`;
        
        // Hide buttons
        document.querySelectorAll('#question-box button').forEach(btn => {
            btn.style.display = 'none';
        });
    }
}

async function submitAnswer(answer) {
    const current = questions[currentQuestionIndex];
    const res = await fetch('/api/validate', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({answer: answer, correct: current.answer})
    });
    const data = await res.json();
    
    if (data.correct) {
        document.getElementById('feedback').textContent = "✅ Correct!";
        score++;
    } else {
        document.getElementById('feedback').textContent = 
            `❌ Wrong! Correct: ${current.answer}`;
    }
    currentQuestionIndex++;
    document.getElementById('score').textContent = 
        `Score: ${score}/${currentQuestionIndex}`;
    setTimeout(showQuestion, 1000);
}


fetchQuestions();
