
quiz = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "What is the color of the sky on a clear day?": "Blue",
    "What is the chemical symbol for water?": "H2O"
}
def kysely(quiz):
    correct_answers_count = 0
    for question, answer in quiz.items():
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            correct_answers_count += 1
        else:
            print("Incorrect. The correct answer is:", answer)
    return correct_answers_count

def start():
    while True:
        play = input("Do you want to start the game? (Y/N) ")
        if play.lower() == "y":
            print("Yay, let's play!")
            # Show questions here and count the score
            score = kysely(quiz) #change this
            display_score(score)
            break
        elif play.lower() == "n":
            print("Thanks for playing!")
            break
        else:
            print("Please write Y or N")

def display_score(score: int):
    print(f"Your final score was: {score}")

if __name__=="__main__":
    start()