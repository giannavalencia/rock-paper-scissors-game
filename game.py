import random

print("Welcome 'Player One' to my Rock, Paper, Scissors, Shoot Game!")
user_choice = input ("Choose 'rock' or 'paper' or 'scissors':")
print("User chose:")
print (user_choice)

options = ["rock", "paper","scissors"]

if user_choice not in options:
    print ("NOT VALID OPTION")
    exit()

computer_choice = random.choice(options)
print("Computer chose:")
print(computer_choice)

#code inspired by Basil Bseiso's on Slack
if(user_choice == "rock" and computer_choice == "scissors"):
    print("YOU WON")
elif(user_choice == "rock" and computer_choice == "paper"):
    print("YOU LOST")
elif(user_choice == "paper" and computer_choice == "scissors"):
    print("YOU LOST")
elif(user_choice == "paper" and computer_choice == "rock"):
    print("YOU WON")
elif(user_choice == "scissors" and computer_choice == "rock"):
    print("YOU LOST")
elif(user_choice == "scissors" and computer_choice == "paper"):
    print("YOU WON")
else: print("TIE")

print("THANKS, PLEASE PLAY AGAIN")
exit()xs