import random # import random module

print("\tWelcome to Guess My Number!")
print("\nI am thinking of a number between 1 and 100.")
print("Try to guess it in a few goes as possible")

the_number = random.randint(1,100) # generate random number
guess = True
tries = 0

while guess != the_number: # This goes on forever as long as you do not find the actual number
    guess = (input("Take a guess "))

    try:
        guess = int(guess)
    except ValueError:
        print("That was not an integer")
    else:
        if guess < 1 or guess > 100:
            print("The number is between 1 and 100")
        elif guess > the_number:
            print("Lower")
        elif guess < the_number:
            print("Higher")
    tries += 1

print("You guessed it! The number was",the_number)
print("And you only took",tries,"tries")



