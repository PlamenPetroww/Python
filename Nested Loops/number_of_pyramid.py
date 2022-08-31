number = int(input())
current = 0
current_equal = False

for row in range(1, number + 1):

    for col in range(1, row + 1):
        current += 1
        print(current, end = " ")
        if current == number:
            current_equal = True
            break
    if current_equal:
        break
    print()
