budget = float(input())
statistic_num = float(input())
price_statistic = float(input())

decor = budget * 0.1
statistic_price = statistic_num * price_statistic
if statistic_num > 150:
    statistic_price *= 0.9
total_price = statistic_price + decor

if total_price > budget:
    money = (abs(total_price - budget))
    print(f"Not enough money!")
    print(f"Wingard needs {money:.2f} leva more.")
else:
    money = (abs(total_price - budget))
    print(f"Action!")
    print(f"Wingard starts filming with {money:.2f} leva left.")







