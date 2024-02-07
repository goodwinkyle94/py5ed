# this is a text file

def my_func():
    do_you_play = input("Do you want to play a game?")
    if do_you_play == "y":
        print("You lose!")
    else:
        print("Correct! The only winnning move is not to play!")
        for i in range(60):
            print("This is a test")
            print("This is a test")
            print("This is a test")


if __name__ == "__main__":
    my_func()
