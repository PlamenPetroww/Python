puzzle = 2.6
speaking_baby = 3
bear = 4.1
minion = 8.2
truck = 2
rent = 0

trip_price = float(input())
puzzle_num = int(input())
speaking_baby_num = int(input())
bear_num = int(input())
minions_num = int(input())
truck_num = int(input())
money = 0
income = 0

total_toys = puzzle_num + speaking_baby_num + bear_num + minions_num + truck_num
total_price = (puzzle_num * puzzle) + (speaking_baby * speaking_baby_num) + (bear * bear_num)\
              + (minion * minions_num) + (truck * truck_num)

if total_toys >= 50:
    total_price *= 0.75

rent = total_price * 0.1
income = total_price - rent

money = round(income - trip_price, 2)

if money < 0:
    print(f"Not enough money! {abs(money):.2f} lv needed.")
else:
    print(f"Yes! {money:.2f} lv left.")


