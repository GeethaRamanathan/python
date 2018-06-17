import random

def dice():
    user_choice = random.randint(1,6)
    print("-----")
    print("|   |")
    print ("| " + str(user_choice)+ " |")
    print("|   |")
    print("-----")
    try_again()

def try_again():
    user_choice = input("Do you want to continue: Y/N")
    if user_choice =="y":
        dice()
    elif user_choice == "n":
        print("Thanks for playing.  See you soon.")
        quit()
    else:
        print("Try again")
        try_again()

dice()
