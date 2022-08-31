budget = float(input())
season = str(input())
count_of_fisherman = int(input())

spring_ship = 3000
ship_summer_autumn = 4200
winter_ship = 2600
ship = 0
money_needed = 0
money_left = 0

if season == "Spring":
    if count_of_fisherman <= 6:
        ship = spring_ship * 0.9
    elif 7 < count_of_fisherman <= 11:
        ship = spring_ship * 0.85
    elif count_of_fisherman >= 12:
        ship = spring_ship * 0.75
elif season == "Summer" or season == "Autumn":
    if count_of_fisherman <= 6:
        ship = ship_summer_autumn * 0.9
    elif 7 < count_of_fisherman <= 11:
        ship = ship_summer_autumn * 0.85
    elif count_of_fisherman >= 12:
        ship = ship_summer_autumn * 0.75
elif season == "Winter":
    if count_of_fisherman <= 6:
        ship = winter_ship * 0.9
    elif 7 < count_of_fisherman <= 11:
        ship = winter_ship * 0.85
    elif count_of_fisherman >= 12:
        ship = winter_ship * 0.75

if count_of_fisherman % 2 == 0 and season != "Autumn":
    ship *= 0.95

if ship > budget:
    money_needed = ship - budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")
elif budget >= ship:
    money_left = budget - ship
    print(f"Yes! You have {money_left:.2f} leva left.")


