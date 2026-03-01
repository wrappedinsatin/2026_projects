num = int(input("Please type in a number: "))

# j increases first, then i

i = 1
j = 1

while i < num:

    while j < num:
        print(f"{i} x {j} = {i * j}")
        j += 1

    i += 1
    j = 1