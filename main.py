def start():
    while True:
        play = input("Do you want to start the game? (Y/N) ")
        if play == "Y":
            print("Yay, let's play!")
        elif play == "N":
            print("Thanks for playing!")
            break
        else:
            print("Please write Y or N")

if __name__=="__main__":
    start()