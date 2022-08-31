video_card = 250

budget = float(input())
video_card_num = int(input())
processor_num = int(input())
ram_num = int(input())

video_card_total = video_card * video_card_num
processor = video_card_total * 0.35
processor_total = processor * processor_num
ram = video_card_total * 0.1
ram_total = ram * ram_num
total_price = video_card_total + processor_total + ram_total

if video_card_num > processor_num:
    total_price *= 0.85

if total_price > budget:
    money_left = (abs(budget - total_price))
    print(f"Not enough money! You need {money_left:.2f} leva more!")
else:
    money_left = budget - total_price
    print(f"You have {money_left:.2f} leva left!")
