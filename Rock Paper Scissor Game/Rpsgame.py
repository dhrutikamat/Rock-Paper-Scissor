"""
WORKFLOW OF PROJECT:
1. Input from user(rock,paper,scissor)
2. Computer choice(Computer will choose randomly not conditionally)
3. Print result

Cases:
1. ROCK
Rock - rock = tie
Rock - paper = Paper win
Rock - scissor = Rock win

2. PAPER
Paper - paper = tie
Paper - scissor = Scissor win
Paper - rock = Paper win

3. SCISSOR
Scissor - scissor = tie
Scissor - rock = Rock win
Scissor - paper = Scissor win

"""

import random
item_list =["Rock","Paper","Scissor"]
user_choice = input("Enter your move = Rock, Paper, Scissor=")
comp_choice = random.choice(item_list)

print(f"user choice = {user_choice}, Computer choice ={comp_choice}")

if user_choice==comp_choice:
    print("Both chooses same: = Match Tie")

elif user_choice=="Rock":
    if comp_choice=="Paper":
        print("Paper covers rock: = Computer wins")
    else:
        print("Rock smashes Scissor: = You win") 

elif user_choice=="Paper":
    if comp_choice== "Scissor":
        print("Scissor cuts paper: = Computer wins")
    else:
        print("Paper wraps rock: = You win")  

elif user_choice=="Scissor":
    if comp_choice=="Rock":
        print("Rock smashes Scissor: = Computer wins")
    else:
        print("Scissor cuts paper: = You win")   



























