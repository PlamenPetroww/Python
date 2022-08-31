teniska = float(input())
limit = int(input())

shorti = teniska * 0.75
chorapi = shorti * 0.2
butonki = (teniska + shorti) * 2
ekip = teniska + shorti + butonki + chorapi
total = (ekip * 0.85)
if total >= limit:
    print(f"Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {abs(total):.2f} lv.")
else:
    needed = abs(total-limit)
    print(f"No, he will not earn the world-cup replica ball.")
    print(f"He needs {needed:.2f} lv. more.")

