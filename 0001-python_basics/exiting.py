import sys

answer = input("Would you like to start the movie? (y/n)  ")
if answer.lower() == "n":
    sys.exit()
else:
    print("Enjoy the show!")


# Use input() to ask the user if they want to start the movie.
# If they answer anything other than "n" or "N", print "Enjoy the show!".
#Otherwise, call sys.exit(). You'll need to import the sys library.
