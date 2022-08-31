student_name = input()
bad_tries = 0
current_class = 1
ist_ejected = False
average_grade = 0
while current_class <= 12:
    current_grade = float(input())
    if current_grade < 4:
        bad_tries += 1
        if bad_tries == 2:
            ist_ejected = True
            break
        continue
    average_grade += current_grade
    current_class += 1

if ist_ejected:
    print(f"{student_name} has been excluded at {current_class} grade")
else:
    grade = average_grade / 12
    print(f"{student_name} graduated. Average grade: {grade:.2f}")