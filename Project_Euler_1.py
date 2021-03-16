sum_up = 0
divided_by_three_and_five = 0
result = 0

for num in range(0, 1000):
    if num % 3 == 0:
        sum_up = sum_up + num

    if num % 5 == 0:
        sum_up = sum_up + num

    if num % 3 == 0 and num % 5 == 0:
        divided_by_three_and_five = divided_by_three_and_five + num

result = sum_up - divided_by_three_and_five
print(result)