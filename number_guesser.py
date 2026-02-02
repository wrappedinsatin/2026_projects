import random

smallest_num = 1
largest_num = 100
is_running = True

print("welcome to the python guessing game!")
print(f"select a number between {smallest_num} and {largest_num}")

while is_running:

    guess = int(input("make your guess!: "))
    correct_num = random.randint(1, 100)

    while guess.isdigit():
        
        while not 1 <= guess <= 100:
            if guess == correct_num:
                print(f"{guess} was the correct number!")
                is_running = False
                break
            elif guess < correct_num:
                print("too low!")
                guess = int(input("make your guess!: "))
            else:
                print("too high!")
                guess = int(input("make your guess!: "))
        else:
            print(f"{guess} is out of range!")
            guess = int(input("make your guess!: "))
    
    else:
        print(f"your 'guess', {guess} is not valid.")
        print(f"your guess must be an integer between {smallest_num} and {largest_num}")
        guess = int(input("make your guess!: "))

play_again = input("would you like to play again? y/n: ")
if play_again.lower == y:
    print("new game started!")
    is_running = True
elif play_again.lower == n:
    print("thanks for playing!")
else:
    print("okay, sure dude. thanks for playing anyway")