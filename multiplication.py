num = int(input("Please type in a number: "))

# j increases first, then i

i = 1
j = 1

while i < num:

    while True:

        print(f"{i} x {j} = {i * j}")
        j += 1

        if j > num:
            i += 1
            j = 1

        if i > num:
            break