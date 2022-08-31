num = int(input())
total_sum_plus = 0
total_sum_minus = 0
total_sum = 0

for numbers in range(num):
    number = int(input())
    if number > 0:
        total_sum_plus += number
    else:
        total_sum_minus -= number
total_sum = total_sum_plus - total_sum_minus
print(total_sum)