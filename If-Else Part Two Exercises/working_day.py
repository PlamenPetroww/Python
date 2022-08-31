day = input()
type_of_the_day = ""

if day == "Monday":
    type_of_the_day = "Working day"
elif day == "Tuesday":
    type_of_the_day = "Working day"
elif day == "Wednesday":
    type_of_the_day = "Working day"
elif day == "Thursday":
    type_of_the_day = "Working day"
elif day == "Friday":
    type_of_the_day = "Working day"
elif day == "Saturday":
    type_of_the_day = "Weekend"
elif day == "Sunday":
    type_of_the_day = "Weekend"
else:
    type_of_the_day = "Error"
print(type_of_the_day)
