from math import floor
numbers_of_tournament = int(input())
starting_points = int(input())
points = 0
win_counter = 0

for numbers in range(numbers_of_tournament):
    current_stage = input()
    if current_stage == "W":
        points += 2000
        win_counter += 1
    elif current_stage == "F":
        points += 1200
    elif current_stage == "SF":
        points += 720
all_points = points + starting_points
average_points = (floor(points / numbers_of_tournament))
win_counter = (win_counter / numbers_of_tournament) * 100
print(f"Final points: {all_points}")
print(f"Average points: {average_points}")
print(f"{win_counter:.2f}%")