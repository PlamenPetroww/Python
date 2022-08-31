n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(n):
    num = int(input())

    if num < 200:
        p1 += 1
    elif num <= 399:
        p2 += 1
    elif num <= 599:
        p3 += 1
    elif num <= 799:
        p4 += 1
    else:
        p5 += 1

p1_counter = p1 / n * 100
p2_counter = p2 / n * 100
p3_counter = p3 / n * 100
p4_counter = p4 / n * 100
p5_counter = p5 / n * 100

print(f"{p1_counter:.2f}%")
print(f"{p2_counter:.2f}%")
print(f"{p3_counter:.2f}%")
print(f"{p4_counter:.2f}%")
print(f"{p5_counter:.2f}%")