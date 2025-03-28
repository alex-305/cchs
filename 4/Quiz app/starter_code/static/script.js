
function getQuizzes() {
    const quizzes = localStorage.getItem('quizzes')
    return quizzes ? JSON.parse(quizzes) : []
}

function saveQuizzes(quizzes) {
    localStorage.setItem('quizzes', JSON.stringify(quizzes))
}

document.addEventListener('DOMContentLoaded', () => {
    const quizList = document.getElementById('quiz-list')

    if(quizList) {
        const quizzes = getQuizzes()

        if(quizzes.length === 0) {
            quizList.innerHTML = "<li>No quizzes available yet.</li>"
        } else {
            quizList.innerHTML = ""

            quizzes.forEach((quiz) => {
                const li = document.createElement('li')
                const a = document.createElement('a')

                a.href = "/quiz/" + quiz.id
                a.textContent = quiz.title

                li.appendChild(a)
                quizList.appendChild(li)

            })
        }

    }

    const createQuizForm = document.getElementById('create-quiz-form')

    if(createQuizForm) {
        createQuizForm.addEventListener('submit', (e) => {
            e.preventDefault()

            const title = document.getElementById('title').value
            let questions = []

            for(let i = 1; i <= 3; i++) {
                const q = document.getElementById('question'+i).value
                const a = document.getElementById('answer'+i).value

                if(q && a) {
                    questions.push({question: q, answer: a})
                }
            }

            if(title && questions.length > 0) {
                const quizzes = getQuizzes()

                const newQuiz = {
                    id: Date.now().toString(),
                    title: title,
                    questions: questions
                }
                quizzes.push(newQuiz)

                saveQuizzes(quizzes)
                window.location.href = "/"
            }

        })
    }
    
    const quizContainer = document.getElementById('quiz-container')

    if(quizContainer) {
        const quizId = quizContainer.dataset.quizId
        const quizzes = getQuizzes()

        const quiz = quizzes.find(q => q.id === quizId)

        if(!quiz) {
            quizContainer.innerHTML = "Quiz not found."
            return
        }

        const form = document.getElementById('quiz-form')
        const questionsDiv = document.getElementById('questions')

        quiz.questions.forEach((q, index) => {
            const div = document.createElement('div')
            const p = document.createElement('p')

            p.textContent = String(index+1) + ". " + q.question
            const input = document.createElement('input')
            input.type = "text"
            input.name = "answer" + index

            div.appendChild(p)
            div.appendChild(input)

            questionsDiv.appendChild(div)
        })

        form.addEventListener('submit', (e) => {
            e.preventDefault()

            let score = 0
            const userAnswers = {}

            quiz.questions.forEach((q, index) => {
                const answerInput = form.elements['answer' + index]
                const userAnswer = answerInput.value

                userAnswers[index] = userAnswer

                if(userAnswer.trim().toLowerCase() === q.answer.trim().toLowerCase()) {
                    score++
                }
            })

            const resultDiv = document.getElementById('result')
            resultDiv.innerHTML = "<h3>Your score: " + score + "/" + quiz.questions.length + "</h3>"


        })
    }
})