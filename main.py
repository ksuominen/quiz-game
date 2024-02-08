quiz = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "What is the color of the sky on a clear day?": "Blue",
    "What is the chemical symbol for water?": "H2O"
}
correct_answers_count = 0
for question, answer in quiz.items():
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        print("Correct!")
        correct_answers_count += 1
    else:
        print("Incorrect. The correct answer is:", answer)