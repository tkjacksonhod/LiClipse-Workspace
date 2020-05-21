'''
Created on Mar 7, 2020

@author: ITAUser
'''
#set variable keepPlaying to true
keepPlaying = True
#While keepPlaying is true:
while(keepPlaying):
    tries = 0
    while(tries < 3):
        #print statement welcoming players to the game
        print("Welcome to Guess the Number!")
        #print statement stating the rules 
        print("Guess the number in 3 or less tries and win, press q to quit game.")
        #import random function - the computer makes its choice randomly from this function
        import random
        #computer's choice = random number between 1 and 15 (random function gets used here) 
        def pick_random_integer(): 
            integer = random.randint(1,15)
            return integer
        computer_pick = random.randint(1,15)
        #player's choice = input(ask player to guess a number) 
        player_pick = random.randint(1,15)
        playerChoice = input("Guess a number between 1 and 15")
        #start checking user guesses
        #if player inputs 'q': -- player wants to end the game
            #else if (player inputs number between 1 and 15 and computer chooses same number)
            #print that they win
        if player_pick == computer_pick:
            print("You win!")
        #else if (player inputs number between 1 and 15 and computer chooses different number)
            #print that they need to guess again
        else:
            print("That's incorrect, guess again.")
            tries += 1
        #else:
            #tell the user their input was not valid
        if pick_random_integer not in range(1,15):
            print("not an option.")
        #print statement thanking the player for playing
        #if (player guesses number in 3 or less guess)
        if tries < 3:
            print("You win! Play again or press q")
        #print that they win
        #else:
            #print that they lost 
        if tries == 3:
            print("You Lose! Try again or press q")
        if (player_pick == "q"):
            print("Thank you for playing!")
