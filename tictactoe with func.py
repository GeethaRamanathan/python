cells = [" "," "," "," "," "," "," "," "," "," "]
count = 0

def display():
    print("%s | %s | %s " %(cells[1],cells[2],cells[3]))
    print("----------")
    print("%s | %s | %s " %(cells[4],cells[5],cells[6]))
    print("----------")
    print("%s | %s | %s " %(cells[7],cells[8],cells[9]))

    get_input()

def get_input():
    global count,cells
    print("Pleast choose from 1 to 9:")
    user_choice1 = int(input("Player 1"))
    user_choice2 = int(input("Player 2"))
    if (cells[user_choice1] == " " and cells[user_choice2] == " "):
        update_cells(user_choice1,user_choice2)
        count+=1
        print(count)
        if(count>2):
            if((cells[1]=='x' and cells[2]=='x' and cells[3]=='x') or \
               (cells[4]=='x' and cells[5]=='x' and cells[6]=='x') or \
               (cells[7]=='x' and cells[8]=='x' and cells[9]=='x') or \
               (cells[1]=='x' and cells[5]=='x' and cells[9]=='x') or \
               (cells[3]=='x' and cells[5]=='x' and cells[7]=='x') or \
               (cells[1]=='x' and cells[4]=='x' and cells[7]=='x') or \
               (cells[2]=='x' and cells[5]=='x' and cells[8]=='x') or \
               (cells[3]=='x' and cells[6]=='x' and cells[9]=='x')):
                print('Player1 wins')
                try_again()
                quit()
            elif ((cells[1]=='o' and cells[2]=='o' and cells[3]=='o') or \
               (cells[4]=='o' and cells[5]=='o' and cells[6]=='o')or \
               (cells[7]=='o' and cells[8]=='o' and cells[9]=='o') or \
               (cells[1]=='o' and cells[5]=='o' and cells[9]=='o') or \
               (cells[3]=='o' and cells[5]=='o' and cells[7]=='o') or \
               (cells[1]=='o' and cells[4]=='o' and cells[7]=='o') or \
               (cells[2]=='o' and cells[5]=='o' and cells[8]=='o') or \
               (cells[3]=='o' and cells[6]=='o' and cells[9]=='o')):
                print('Player2 wins')
                try_again()
                quit()
            else:
                print("No one wins.....")
                try_again()
                
    else:
        print("Cell is occupied")

    display()

def update_cells(user_choice1, user_choice2):
    cells[user_choice1] = "x"
    cells[user_choice2] = "o"


def try_again():
    global cells,count
    user_input = input("Do you want to play again(Y/N)")
    if user_input=='Y' or user_input =='y':
        cells = [" "," "," "," "," "," "," "," "," "," "]
        count=0
        get_input()
    else:
        print("Thanks for playing")
        quit()


display()
