# Paste your code into this box
guess = 50
inputv = ["h", "l", "c"]
indicator = "a"
min = 0
max = 100

#standard case
print("Please think of a number between 0 and 100!")
print("Is your secret number " + str(guess) + "?")
indicator = str(input("Enter 'h' tp indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))

while not(indicator in inputv):
    print("Sorry, I did not understand your input.")
    print("Is your secret number " + str(guess) + "?")
    indicator = str(input("Enter 'h' tp indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))

#while guess is not correct
while indicator != "c":
    if indicator == "h":
        #new borders
        max = guess
        guess = min + (max - min)//2
        print("Is your secret number " + str(guess))
        indicator = str(input("Enter 'h' tp indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
        if not(indicator in inputv):
                    while not(indicator in inputv):
                        print("Sorry, I did not understand your input.")
                        print("Is your secret number " + str(guess) + "?")
                        indicator = str(input("Enter 'h' tp indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
            
    elif indicator == "l":
        #new borders
        min = guess
        guess = min + (max - min)//2
        print("Is your secret number " + str(guess))    
        indicator = str(input("Enter 'h' tp indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
        if not(indicator in inputv):
            while not(indicator in inputv):
                        print("Sorry, I did not understand your input.")
                        print("Is your secret number " + str(guess) + "?")
                        indicator = str(input("Enter 'h' tp indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))


if indicator == "c":
    print("Game over. Your secret number was: " + str(guess))