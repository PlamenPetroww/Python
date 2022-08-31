budget = float(input())
season = input()
destination = ""
nights = ""
total = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        nights = "Camp"
        total = budget * 0.3
    elif season == "winter":
        nights = "Hotel"
        total = budget * 0.7
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        nights = "Camp"
        total = budget * 0.4
    elif season == "winter":
        nights = "Hotel"
        total = budget * 0.8
elif budget > 1000:
    nights = "Hotel"
    destination = "Europe"
    total = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{nights} - {total:.2f}")
