days_of_stay = int(input())
room = input()
attitude = input()

room_for_one_person = 18.00
apartment_for_one_person = 25.00
president_apartment = 35.00
night = days_of_stay - 1
money_needed = 0
total = 0

if room == "room for one person":
    money_needed = night * room_for_one_person
    total = money_needed

elif room == "apartment":
    if night < 10:
        money_needed = apartment_for_one_person * night
        total = money_needed * 0.7
    elif 10 <= night <= 15:
        money_needed = apartment_for_one_person * night
        total = money_needed * 0.65
    elif night > 15:
        money_needed = apartment_for_one_person * night
        total = money_needed * 0.5

elif room == "president apartment":
    money_needed = president_apartment * night
    total = money_needed * 0.9
    if 10 <= night <= 15:
        money_needed = president_apartment * night
        total = money_needed * 0.85
    elif night > 15:
        money_needed = president_apartment * night
        total = money_needed * 0.8

if attitude == "positive":
    total = total * 1.25
elif attitude == "negative":
    total = total * 0.9
print(f"{total:.2f}")





