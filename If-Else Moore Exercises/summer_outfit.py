
grad = int(input())
weather = input()
outfit = ""
shoes = 2

if 10 <= grad <= 18:
    if weather == "Morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif weather == "Afternoon":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif weather == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
elif 18 < grad <= 24:
    if weather == "Morning":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif weather == "Afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif weather == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
elif grad >= 25:
    if weather == "Morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif weather == "Afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
    elif weather == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
print(f"It's {grad} degrees, get your {outfit} and {shoes}.")