# A programmer is developing a "Who am I?" game. 
# The user is given five clues and they must guess who the celebrity is. 
# The game ends when the celebrity's name is guessed. 
# Construct an algorithm for this game. (choose an arbitrary celebrity)

celebrity = "Keanu Reeves"
guess = input("Your guess: ")
clues = ["This celebrity is an actor","This celebrity acted in a famous trilogy movie series","This celebrity has a role in the video game Cyberpunk 2077","The first letter of this celebrity's name is K","The last name of this celebrity is Reeves"]
clue = 0
while guess.lower() != celebrity.lower():
    print("Wrong Guess! Try again...")
    print(f"Here is a hint: {clues[clue]}\n")

# maybe implement later with recursion?
    clue += 1
    if clue > len(clues)-1:
        clue=0
    guess=input("Your guess: ")

print("You won!")