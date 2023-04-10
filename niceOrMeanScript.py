#
# Python 3.10.6
#
# Author: Lily F. Kiousis
#
# Purpose: The Tech Academy - creating a game in Python.
#          Demonstrating how to pass varaibles from function to function.
#          We are going to be creating a functional game to do so.
#
#          Remember, function_name(variable) means that we pass in the
#          varaible. return variable means that we are returning the variable
#          back to the calling function.


from playsound import playsound

def start(nice=0, mean=0, name=""): #='s (parameters) so that the game doesn't error if no user input is given.
    #get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)
    

def describe_game(name):
    """
        check if this is a new game or not.
        If it is new, get user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game.
    """
    #meaning, if we do not already have this user's name,
    # then they are a new player and we need to get their name
    if name!= "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True 
        while stop: #While name is empty run name input
            if name == "":
                playsound('StartOver.wav')
                name = input("\nWhat's your name? \n>>> ").capitalize() #Capitalizes the user input
                if name != "": #If name is not empty run print below
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of your game your fate \n will be sealed by your actions.")
                    stop = False #Shuts off this particular block of code bc we have user's name and can move on.
    return name


def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower() #Makes input lower case for program's sake.
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1) #changes value of nice if picked by 1. So mean = 0, nice = 1, name= "".
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = (mean + 1) #Changes value, same as nice notation.
            stop =  False
    score(nice,mean,name) # pass the 3 variables to the score()


def show_score(nice,mean,name):
    print("\n{}, your current total is: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))


def score(nice,mean,name):
    # score function is being passed the calue stored within the 3 varaibles
    if nice > 2: #if condition is valid, call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 2: #if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else: #else, call nice_mean function passing in the variables so it can use them, aka continue playing until win or lose
          #conditions are met
        nice_mean(nice,mean,name)


def win(nice,mean,name):
    #Substitute wildcards with the variable values
    print("\nNice job {}, you win! \nYou are well-liked and you've \nmade lots of friends along the way!".format(name))
    #call again function and pass in our variables
    again(nice,mean,name)


def lose(nice,mean,name):
    #Substitute {} wildcards with the variable values
    print("\nGosh darn it, game over! \n{}, you are forced to apologize \nto those you were mean to \nand make amends!".format(name))
    #call again function and pass in our variables
    again(nice,mean,name)


def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (Y/N):\n>>>".lower())
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO'\n>>> ")


def reset(nice,mean,name):
    nice = 0
    mean = 0
    #Here we do not include name since the same player has selected to play again.
    start(nice,mean,name)







# Tells python we are running this code as a script and to run everything
# underneath. start() would be the first function to fire off.
if __name__ == "__main__": 
    start()
