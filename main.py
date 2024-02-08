def start():
    while True:
        play = input("Do you want to start the game? (Y/N) ")
        if play.lower() == "y":
            print("Yay, let's play!")
            # Show questions here and count the score
            score = 10 #change this
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