month = input()
nights = int(input())
studio = 0
apartment = 0
money_for_apartment = 0
money_for_studio = 0

if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if 7 < nights < 14:
        studio *= 0.95
    elif nights > 14:
        studio *= 0.7
elif month == "June" or month == "September ":
    studio = 75.2
    apartment = 68.7
    if nights > 14:
        studio *= 0.8
elif month == "July" or month == "August":
    studio = 76
    apartment = 77
if nights > 14:
    apartment *= 0.9

money_for_apartment = nights * apartment
money_for_studio = nights * studio

print(f"Apartment: {money_for_apartment:.2f} lv.")
print(f"Studio: {money_for_studio:.2f} lv.")
