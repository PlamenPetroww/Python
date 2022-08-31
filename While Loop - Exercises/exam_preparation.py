number_of_bad_grades = int(input())

counter_of_bad_grades = 0
good_grades = 0
count_of_problems = 0
has_passed = True
last_problem = ""
first_exercise = input()

while first_exercise != "Enough":
    last_problem = first_exercise
    grade = float(input())
    count_of_problems += 1
    good_grades += grade

    if grade <= 4:
        counter_of_bad_grades += 1
        if counter_of_bad_grades == number_of_bad_grades:
            print(f"You need a break, {counter_of_bad_grades} poor grades.")
            has_passed = False
            break
    first_exercise = input()

if has_passed:
    print(f"Average score: {good_grades / count_of_problems:.2f}")
    print(f"Number of problems: {count_of_problems}")
    print(f"Last problem: {last_problem}")

