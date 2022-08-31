age = int(input())
laundry_price = float(input())
toy_price = int(input())
money_saved = 0
toys_count = 0
amount = 0

for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        amount += 10
        money_saved += amount - 1
    else:
        toys_count += 1
money_saved += toy_price * toys_count

if money_saved >= laundry_price:
    print(f"Yes! {money_saved - laundry_price:.2f}")
else:
    print(f"No! {abs(laundry_price - money_saved):.2f}")

