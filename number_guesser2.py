# functions functions functions!

import random

smallest_num = 1
biggest_num = 100

def play_game():
    
    correct_num = random.randint({smallest_num}, {biggest_num})
    print("welcome to my number guessing game!")
    print(f"select a number between {smallest_num} and {biggest_num}")

    while True:
        guess = input("make your guess!: ")
        try:
            guess = int(guess)
        except ValueError:
            print(f"{guess} was not valid!")
            print(f"your guess must be an INTEGER between {smallest_num} and {biggest_num}")
            continue
    
        if not ({smallest_num} <= guess <= {biggest_num}):
            print(f"{guess} is out of range!")
            print(f"make sure you typed in an integer between {smallest_num} and {biggest_num}!")
        else:
            continue

        if guess == correct_num:
            print(f"{guess} was the correct number!")
            print("congratulations! you won!")
            break
        elif guess < correct_num:
            print(f"{guess} was too low!")
        else:
            print(f"{guess} was too high!")

def main():
    while True:
        play_game()
        play_again = input("would you like to play again? y/n: ").lower()
        if play_again == "y":
            print("new game started!")
            break # breaks inner loop, play_game() is executed
        elif play_again == "n":
            print("thanks for playing!")
            break
        else:
            print("please select y or n")

if __name__ == "__main__":
    main()

