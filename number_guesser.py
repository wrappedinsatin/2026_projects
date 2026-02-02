import random

smallest_num = 1
largest_num = 100
is_running = True

print("welcome to the python guessing game!")
print(f"select a number between {smallest_num} and {largest_num}")
correct_num = random.randint(1, 100)

while is_running:
    guess = int(input("make your guess!: "))
    while not guess.isdigit():
        print(f"your 'guess', {guess} is not valid.")
        print(f"your guess must be an integer between {smallest_num} and {largest_num}")
        guess = int(input("make your guess!: "))

             
