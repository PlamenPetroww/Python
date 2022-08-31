
computer = int(input())
possible_money = int(input())


for number in range(0, computer + 1):
    possible_money = str(number)
    for index, digit in enumerate(possible_money):
        if index % 3 === 0