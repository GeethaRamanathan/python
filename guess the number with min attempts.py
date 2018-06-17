import random
import time

def gwat():
    attempts = 5
    win = False
    computer_choice = random.randint(1,100)

    while attempts > 0:
         user_choice = int(input("Guesst the number between 1 and 100:"))
         attempts-=1
         if computer_choice > user_choice:
             print("You lose. Your choice is less than computer's choice.")
             print(difference(computer_choice, user_choice))
             print("Only",attempts, "attempts left")
             
         elif computer_choice < user_choice:
             print("You lose. Your choice is greater than computer's choice.")
             print(difference(computer_choice, user_choice))
             print("Only", attempts ,"attempts left")

         else:
             print("You win.  Your choice is same as computer's choice.")
             win = True
             try_again()

         

    if win == False:
        print("Your chances are over.")
        try_again()

def try_again():
    user_choice = input("Do you want to continue:y/n")
    if user_choice == "y":
        gwat()
    else:
        print("Thanks for playing.")
        time.sleep(5)
        quit()

def difference(computer_choice, user_choice):
    diff= abs(computer_choice - user_choice)
    return diff

gwat()
