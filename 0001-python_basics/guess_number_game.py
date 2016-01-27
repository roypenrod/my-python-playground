import random

# generate a secret random number between 1 and 10
secret_number = random.randint(1, 10)

# greeting and instructions
print (" ")
print("I have secretly chosen a number between 1 and 10.")
print("The secret number can include 1 and 10.")
print("Guess what my number is and I won't delete your hard drive.")
print("Just kidding.  Maybe. ;-)")
print(" ")

# set up the game loop
while True:
    # get a number guess from the player
    guess = int(input("What is my number?\n"))
    # compare guess to secret number
    if guess == secret_number:
        print("Awww. :-(  You guessed my number.")
        print("Sigh.  I'll get you next time.")
        print("<restoring all deleted files>")
        print(" ")
        break
    # let player know if it was a hit or a miss
    else:
        print("Hahaha!  You didn't get it!  I'll just take that file")
        print("right ... over ... there.")
        print("<file deleted>")
        print(" ")
