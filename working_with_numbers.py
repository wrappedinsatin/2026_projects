print("Please type in integer numbers. Type in 0 to finish")
num_count = 0
num_list = []

while True:
    new_num = int(input("Number: "))

    if new_num != 0:
        num_list.append(new_num)
        num_count += 1
    else:
        break

print(f"Numbers typed in: {num_count}")

sum_numbers = 0
for num in num_list:
    sum_numbers += num

print(f"The sum of the numbers is {sum_numbers}")

mean = sum_numbers / num_count

print(f"The mean of the numbers is {mean}")

pos_nums = 0
neg_nums = 0

for num in num_list:
    if num > 0:
        pos_nums += 1
    else:
        neg_nums += 1

print(f"Positive numbers {pos_nums}")
print(f"Negative numbers {neg_nums}")
