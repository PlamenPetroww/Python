Roses_price = 5
Dahlias_price = 3.8
Tulips_price = 2.8
Narcissus_price = 3
Gladiolus_price = 2.5

flowers = str(input())
numbers_of_flowers = int(input())
budget = int(input())
total = 0
money = 0

if flowers == "Roses":
    total = Roses_price * numbers_of_flowers
    if numbers_of_flowers > 80:
        total = total - total * 0.1
elif flowers == "Tulips":
    total = Tulips_price * numbers_of_flowers
    if numbers_of_flowers > 80:
        total = total - total * 0.15
elif flowers == "Dahlias":
    total = Dahlias_price * numbers_of_flowers
    if numbers_of_flowers > 90:
        total = total - total * 0.15
elif flowers == "Narcissus":
    total = Narcissus_price * numbers_of_flowers
    if numbers_of_flowers < 120:
        total = total + total * 0.15
elif flowers == "Gladiolus":
    total = Gladiolus_price * numbers_of_flowers
    if numbers_of_flowers < 80:
        total = total + total * 0.2

if budget >= total:
    money = budget - total
    print(f"Hey, you have a great garden with {numbers_of_flowers} {flowers} and {money:.2f} leva left.")
elif budget < total:
    money = total - budget
    print(f"Not enough money, you need {money:.2f} leva more.")
