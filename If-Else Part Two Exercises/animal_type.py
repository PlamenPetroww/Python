animal = input()
animal_type = ""

if animal == "dog":
    animal_type = "mammal"
elif animal == "snake" or animal == "crocodile" or animal == "tortoise":
    animal_type = "reptile"
else:
    animal_type = "unknown"
print(animal_type)