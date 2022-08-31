age = float(input())
male = input()

if male == "m" and age >= 16:
    print("Mr.")
elif male == "m" and age < 16:
    print("Master")
elif male == "f" and age >= 16:
    print("Ms.")
elif male == "f" and age < 16:
    print("Miss")