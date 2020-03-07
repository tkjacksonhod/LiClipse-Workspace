'''
Created on Feb 1, 2020

@author: ITAUser
'''
#set variable keepPlaying to true
keepPlaying = True 
#While keepPlaying is true:
while (keepPlaying):
    print("Welcome to Rock Paper Scissors!")
    #print statement welcoming players to the game
    #print statement stating the rules (best 2 out of 3 press 'q' to quit)
    print("Best 2 out of 3 wins, press 'q' to quit the game.")
    #make a key that assigns a number to each choice for the computer
    Rock = 1
    Paper = 2
    Scissors = 3
    #(rock is 1, scissors is 2, paper is 3)
    #import random function - the computer makes its choice randomly from this function
    import random 
    #set computer's score to 0
    computer = 0
    #set player's score to 0
    player = 0
    #while player's score is less than 2 and the computer's score is less than 2; -- this means that the game is still on
    while computer > 2:
        
        #computer's choice = random number between 1 and 3 (random function gets used here)
        computer_pick = random.randint(1,3)
        #player's choice = input(ask player to select Rock, Paper, or Scissors) 
        player_pick = random.randint(1,3) 
        #start checking user options
        #userChoice = userChoice.lower()
        #if player inputs 'q': -- player wants to end the game
        if player_pick == "q":
            print("Player quit game")
        #set keepPlaying to False -- ends the loop
        #stop the loop -- whoo! break statement
        #else if (player inputs rock and computer chooses rock) or
        elif ((player_pick == 1) and (computer_pick == 1)) or ((player_pick == 2) and (computer_pick == 2)) or ((player_pick == 3 and computer_pick == 3)):
            print("DRAW")
            print("Player Score: 0 and Computer Score: 0")
        #(player inputs paper and computer chooses paper) or 
        #(player inputs scissors and computer chooses scissors): 
        #print out DRAW
        #print out player's score and computer's score 
        #else if (player inputs rock and computer chooses scissors) or 
        #(player inputs scissors and computer chooses paper) or 
        #(player inputs paper and computer chooses rock):
        #add one to the player's score 
        #print out player's score and computer's score 
        elif ((player_pick == 1) and (computer_pick == 3)) or ((player_pick == 3) and (computer_pick == 2)) or ((player_pick == 2) and (computer_pick == 1)):
            print(player)
            player += 1
        #else if (player inputs rock and computer chooses paper) or
        #(player inputs paper and computer chooses scissors) or
        #(player inputs scissors and computer chooses rock):
        #add one to the computer's score 
        #print out player's score and computer's score
        elif ((player_pick == 1) and (computer_pick == 2)) or ((player_pick == 2) and (computer_pick == 3)) or ((player_pick == 3) and (computer_pick == 1)):
            print(computer)
            computer += 1 
        #else:
        else:
            print("Invalid input, try again.")
            #tell the user their input was not valid
        #print statement thanking the player for playing
        print("Thank you for playing!")
        #if player's score is 2:
        if player == 2:
            print("Good job, you won!")
            #print statement letting player know they won
        #if computers score is 2:
        if computer == 2:
            print("Better luck next time, you lost.")
            #print out statement letting player know the computer won
        #print out player's score and computer's score
        print (player and computer)