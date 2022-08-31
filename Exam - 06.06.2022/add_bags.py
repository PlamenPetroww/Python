luggage = float(input())
luggage_for_kg = int(input())
days = int(input())
num_of_luggage = int(input())
cena = 0

if luggage_for_kg < 10:
    cena = luggage * 0.2
elif luggage_for_kg >= 10 and luggage_for_kg <= 20:
    cena = luggage * 0.5
elif luggage_for_kg > 20:
    cena = luggage

if days > 30:
    cena *= 1.1
elif days <= 30 and days >= 7:
    cena *= 1.15
elif days < 7:
    cena *= 1.4

obshta_cena = cena * num_of_luggage

print(f"The total price of bags is: {obshta_cena:.2f} lv.")