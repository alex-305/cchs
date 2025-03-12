// Get quizzes from localStorage (returns an array)
function getQuizzes() {
    const quizzes = localStorage.getItem('quizzes');
    return quizzes ? JSON.parse(quizzes) : [];
}

// Save the quizzes array back to localStorage
function saveQuizzes(quizzes) {
    localStorage.setItem('quizzes', JSON.stringify(quizzes));
}

document.addEventListener('DOMContentLoaded', () => {
    // Index page: display list of quizzes
    const quizList = document.getElementById('quiz-list');
    if (quizList) {
        const quizzes = getQuizzes();
        if (quizzes.length === 0) {
            quizList.innerHTML = "<li>No quizzes available yet.</li>";
        } else {
            quizList.innerHTML = "";
            quizzes.forEach((quiz) => {
                const li = document.createElement('li');
                const a = document.createElement('a');
                a.href = `/quiz/${quiz.id}`;
                a.textContent = quiz.title;
                li.appendChild(a);
                quizList.appendChild(li);
            });
        }
    }
    
    // Create quiz page: intercept form submission and save new quiz
    const createQuizForm = document.getElementById('create-quiz-form');
    if (createQuizForm) {
        createQuizForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const title = document.getElementById('title').value;
            let questions = [];
            for (let i = 1; i <= 3; i++) {
                const q = document.getElementById(`question${i}`).value;
                const a = document.getElementById(`answer${i}`).value;
                if (q && a) {
                    questions.push({question: q, answer: a});
                }
            }
            if (title && questions.length > 0) {
                const quizzes = getQuizzes();
                // Use a timestamp as a simple unique ID
                const newQuiz = {
                    id: Date.now().toString(),
                    title: title,
                    questions: questions
                };
                quizzes.push(newQuiz);
                saveQuizzes(quizzes);
                window.location.href = '/';
            }
        });
    }
    
    // Take quiz page: load quiz by id, display questions, and handle submission
    const quizContainer = document.getElementById('quiz-container');
    if (quizContainer) {
        const quizId = quizContainer.dataset.quizId;
        const quizzes = getQuizzes();
        const quiz = quizzes.find(q => q.id === quizId);
        if (!quiz) {
            quizContainer.innerHTML = "Quiz not found.";
            return;
        }
        
        const form = document.getElementById('quiz-form');
        const questionsDiv = document.getElementById('questions');
        
        // Dynamically create input fields for each question
        quiz.questions.forEach((q, idx) => {
            const div = document.createElement('div');
            const p = document.createElement('p');
            p.textContent = `${idx + 1}. ${q.question}`;
            const input = document.createElement('input');
            input.type = 'text';
            input.name = `answer${idx}`;
            input.required = true;
            div.appendChild(p);
            div.appendChild(input);
            questionsDiv.appendChild(div);
        });
        
        // Process answers and show results
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            let score = 0;
            const userAnswers = {};
            quiz.questions.forEach((q, idx) => {
                const answerInput = form.elements[`answer${idx}`];
                const userAnswer = answerInput.value;
                userAnswers[idx] = userAnswer;
                if (userAnswer.trim().toLowerCase() === q.answer.trim().toLowerCase()) {
                    score++;
                }
            });
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = `<h3>Your Score: ${score} / ${quiz.questions.length}</h3>`;
            const ul = document.createElement('ul');
            quiz.questions.forEach((q, idx) => {
                const li = document.createElement('li');
                li.innerHTML = `<strong>Question ${idx+1}:</strong> ${q.question}<br>
                <em>Your answer:</em> ${userAnswers[idx]}<br>
                <em>Correct answer:</em> ${q.answer}`;
                ul.appendChild(li);
            });
            resultDiv.appendChild(ul);
        });
    }
});
