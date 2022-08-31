numbers_of_group = int(input())
all_people = 0
people = 0
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0

for numbers in range(numbers_of_group):
    people_in_one_group = int(input())
    all_people += people_in_one_group
    if people_in_one_group <= 5:
        musala += people_in_one_group
    elif 6 <= people_in_one_group <= 12:
        monblan += people_in_one_group
    elif 13 <= people_in_one_group <= 25:
        kilimandjaro += people_in_one_group
    elif 26 <= people_in_one_group <= 40:
        k2 += people_in_one_group
    elif people_in_one_group >= 41:
        everest += people_in_one_group

people_for_musala = musala / all_people * 100
people_for_monblan = monblan / all_people * 100
people_for_kilimandjaro = kilimandjaro / all_people * 100
people_for_k2 = k2 / all_people * 100
people_for_everest = everest / all_people * 100

print(f"{people_for_musala:.2f}%")
print(f"{people_for_monblan:.2f}%")
print(f"{people_for_kilimandjaro:.2f}%")
print(f"{people_for_k2:.2f}%")
print(f"{people_for_everest:.2f}%")


