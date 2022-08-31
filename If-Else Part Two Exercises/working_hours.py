hours = int(input())
day = str(input())

if 10 <= hours <= 18 and day != "Sunday":
    print("open")
else:
    print("closed")