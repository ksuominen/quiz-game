import json


def load_quiz(filename: str):
    with open(filename) as json_file:
        quiz = json.load(json_file)
        return quiz


def kysely(quiz: dict):
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
            try:
                quiz = load_quiz("quiz1.json")
            except:
                print("Sorry, an error occured while loading the quiz")
                break
            score = kysely(quiz)
            display_score(score, len(quiz))
            break
        elif play.lower() == "n":
            print("Thanks for playing!")
            break
        else:
            print("Please write Y or N")


def display_score(score: int, max_score: int):
    print(f"Your final score was: {score}/{max_score}")


if __name__ == "__main__":
    start()

