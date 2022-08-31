first_number = int(input())
second_number = int(input())
operator = str(input())
total_sum = 0
odd_or_even = ""

if operator == "+" and first_number != 0 and second_number != 0:
    total_sum = first_number + second_number
    if total_sum % 2 == 0:
        odd_or_even = "even"
    else:
        odd_or_even = "odd"
elif operator == "-" and first_number != 0 and second_number != 0:
    total_sum = first_number - second_number
    if total_sum % 2 == 0:
        odd_or_even = "even"
    else:
        odd_or_even = "odd"
elif operator == "*" and first_number != 0 and second_number != 0:
    total_sum = first_number * second_number
    if total_sum % 2 == 0:
        odd_or_even = "even"
    else:
        odd_or_even = "odd"
elif operator == "/":
    if second_number != 0:
        total_sum = first_number / second_number
elif operator == "%":
    if second_number != 0:
        total_sum = first_number % second_number
if operator == "+" or operator == "-" or operator == "*":
    print(f"{first_number} {operator} {second_number} = {total_sum} - {odd_or_even}")
elif operator == "%" or operator == "/":
    if second_number == 0:
        print(f"Cannot divide {first_number} by zero")
    elif operator == "/":
        print(f"{first_number} {operator} {second_number} = {total_sum:.2f}")
    elif operator == "%":
        print(f"{first_number} {operator} {second_number} = {total_sum}")
