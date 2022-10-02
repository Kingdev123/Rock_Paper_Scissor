import random
import math

def Rock_Paper_Scissor():
    user = input("Enter your choice: 'r' for rock, 'p' for paper, 's' for scissor\n")
    user = user.lower()
    
    computer = random.choice(['r','p','s'])
    
    if user == computer:
        return (0, user, computer)
    
# r>s, s>p, p>r
    if win(user, computer):
        return (1, user, computer)
    
    return (-1, user, computer)

def win(x,y):
    # return true is the player beats the opponent
    if (x == 'r' and y == 's') or (x == 's' and y == 'p') or (x == 'p' and y == 'r'):
        return True
    return False

def Best_of(n):
    user_win=0
    computer_win =0
    wins_needed= math.ceil(n/2)
    
    while user_win<wins_needed and computer_win<wins_needed:
        result, user, computer = Rock_Paper_Scissor()
        #tie
        if result == 0:
            print("its a tie. {}".format(computer))
        #win
        elif result == 1:
            user_win += 1
            print("you: {}, computer: {}. You won!!!".format(user,computer))
        else:
            computer_win += 1
            print("you: {}, computer:{}. You lost :(".format(user,computer))
        print('\n')
        
    if user_win > computer_win:
        print("you have won best of {} games CHAMP!!! :)".format(n))
    else:
        print("the computer has won best of {} games LOSERR!!! :(".format(n))
        
Best_of(3)
