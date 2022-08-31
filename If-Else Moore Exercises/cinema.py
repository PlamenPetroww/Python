premiere_ticket = 12
normal_ticket = 7.5
discount = 5

typ_projection = input()
rows = int(input())
cols = int(input())
money = 0

if typ_projection == "Premiere":
    money = rows * cols * premiere_ticket
elif typ_projection == "Normal":
    money = rows * cols * normal_ticket
elif typ_projection == "Discount":
    money = rows * cols * discount
print(f"{money:.2f} leva")
