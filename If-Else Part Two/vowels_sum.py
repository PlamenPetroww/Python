word = str(input())
a = 1
e = 2
i = 3
o = 4
u = 5
total = 0

for asd in range(0, len(word)):
    if word[asd] == "a":
        total += 1
    if word[asd] == "e":
        total += 2
    if word[asd] == "i":
        total += 3
    if word[asd] == "o":
        total += 4
    if word[asd] == "u":
        total += 5
print(total)