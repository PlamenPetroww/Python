movie_name = input()

student_tickets = 0
standard_tickets = 0
kids_tickets = 0


while movie_name != "Finish":
    seats_taken = 0
    free_seats = int(input())

    ticket_type = str(input())
    while ticket_type != "End":
        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kids_tickets += 1

        seats_taken += 1
        if free_seats - seats_taken == 0:
            break
        ticket_type = input()
    print(f"{movie_name} - {seats_taken / free_seats * 100:.2f}% full.")
    movie_name = input()

all_tickets = standard_tickets + student_tickets + kids_tickets
print(f"Total tickets: {all_tickets}")
print(f"{student_tickets / all_tickets * 100:.2f}% student tickets.")
print(f"{standard_tickets / all_tickets * 100:.2f}% standard tickets.")
print(f"{kids_tickets / all_tickets * 100:.2f}% kids tickets.")
