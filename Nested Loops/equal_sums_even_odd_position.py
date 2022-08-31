first_num = int(input())
second_num = int(input())

for number in range(first_num, second_num + 1):
    even_sum = 0
    odd_sum = 0
    for index, digit in enumerate(str(number)):
        if (index + 1) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    if odd_sum == even_sum:
        print(number, end = " ")
