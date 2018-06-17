import random

dict = {1:'rock',2:'paper',3:'scissor'}

def play():
    computer_choice = random.randint(1,3)
##print(dict[computer_choice])
    user_choice = int(input("1.Rock  2.Paper  3.Scissor"))
##print(dict[user_choice])

    if computer_choice == 1 and user_choice == 1:
        print("Computers choice:"+dict[computer_choice]+"\n" + "Yours choice:" +dict[user_choice])
        print("Tie")
        try_again()
    elif computer_choice == 1 and user_choice == 2:
        print("Computers choice:"+dict[computer_choice]+"\n" + "Yours choice:" +dict[user_choice])
        print("You won")
        try_again()
    elif computer_choice == 1 and user_choice == 3:
        print("Computers choice:"+dict[computer_choice]+"\n" + "Yours choice:" +dict[user_choice])
        print("You lose")
        try_again()
    elif computer_choice == 2 and user_choice == 1:
        print("Computers choice:"+dict[computer_choice]+"\n" + "Yours choice:" +dict[user_choice])
        print("You lose")
        try_again()
    elif computer_choice == 2 and user_choice == 2:
        print("Computers choice:"+dict[computer_choice]+"\n" + "Yours choice:" +dict[user_choice])
        print("Tie")
        try_again()
    elif computer_choice == 2 and user_choice == 3:
        print("Computers choice:"+dict[computer_choice]+"\n" + "Yours choice:" +dict[user_choice])
        print("You Won")
        try_again()
    elif computer_choice == 3 and user_choice == 1:
        print("Computers choice:"+dict[computer_choice]+"\n" + "Yours choice:" +dict[user_choice])
        print("You Lose")
        try_again()
    elif computer_choice == 3 and user_choice == 2:
        print("Computers choice:"+dict[computer_choice]+"\n" + "Yours choice:" +dict[user_choice])
        print("You won")
        try_again()
    elif computer_choice ==3 and user_choice == 3:
        print("Computers choice:"+dict[computer_choice]+"\n" + "Yours choice:" +dict[user_choice])
        print("Tie")
        try_again()
    else:
        try_again()

def try_again():
    user_choice = input("Do you want to continue (y/n):")
    if user_choice =='y' or user_choice =='Y':
        play()
    else:
        print("Thanks for playing")

play()
