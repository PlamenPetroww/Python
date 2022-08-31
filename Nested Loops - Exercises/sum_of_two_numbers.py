a = int(input())
b = int(input())
c = int(input())
combinations = 0
combination_is_found = False

for x1 in range(a, b + 1):
    for x2 in range(a, b + 1):
        combinations += 1
        if x1 + x2 == c:
            combination_is_found = True
            break
    if combination_is_found:
        break
if combination_is_found:
    print(f"Combination N:{combinations} ({x1} + {x2} = {c})")
else:
    print(f"{combinations} combinations - neither equals {c}")