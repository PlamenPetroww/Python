from math import pi

figure = input()
result = 0
if figure == "square":
    side = float(input())
    result = side * side
elif figure == "rectangle":
    side = float(input())
    side_a = float(input())
    result = side * side_a
elif figure == "circle":
    radius = float(input())
    result = pi * (radius ** 2)
else:
    side = float(input())
    height = float(input())
    result = side * height / 2
print(f"{result:.3f}")


