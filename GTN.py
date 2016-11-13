#Author(alias): Genkaku
#Date: 13/10/16

#imports
import random #imports the random function
import splash
#functions
def nGen():#created a block called nGen(number generator)
    try:#try code below
        num = random.randint(0,int(input('Pick the heighest number this will generate: ')))#create a variable called num and makes it equal to a number between 0 and a number of the users choice
        return num#returns the variable num to the code block 'main'
    except:#if there is an error it will run the code below
        print('Invalid input, defaulting to 100')#message alerting the user that the input wasn't valid 
        num = random.randint(0,100)# sets the variable num to a number between 0 and 100
        return num# returns the variable num

def main():#creates the code block main
    prev = []#creates the array prev
    guess = ''#creates the variable guess
    print('Welcome to guess the number by Genkaku!')#program welcomes the user
    num = nGen()#num will be set to the returned value of nGen
    IO(num,prev,guess)#passes the variables 'num','prev' and 'guess'

            
                     
def IO(num,prev,guess):#creates the code block IO
    try:#tries the code below
        print('Please guess the number.')#prompts the user to guess a number
        guess = int(input('>'))#creates the variable called guess and makes it equal to the users input
        prev.append(guess)#adds the guess to the array 'preb'
        print('Guesses:',prev)#prints the word guess with the numbers previously used by the user
        if guess > num:# checksif guess is bigger than the number
            print('Too high!')#tells the user if its too high
            IO(num,prev,guess)#calls the block
        elif guess < num:#checks if the guess is less than the number
            print('Too low!')#tells the user if their guess is too low
            IO(num,prev,guess)#calls the block
        elif guess == num:#checks if the guess is the same as the number
            print('Thats right!')#tells the user they are correct
            print('You got it in',len(prev),'tries!')#tells the user how many tries it took
            guess = input('Play again Y/N: ')#gives the player the option to play again
            if guess.lower() == 'y':#checks if the input is equal to y
                main()#it calls the start of the program again
            else:#if it isn't equal to y assume they want to quit
                print('Bye!')#says goodbye to the user
    except:#if this fails
        print('Invalid input')#tell the user their input was incorrect
        IO(num,prev,guess)#calls the block again

#controller
if __name__ == '__main__':#checks if the program has been imported
    main()#calls the program again
