jury = int(input())

presentation_name = input()
avv_score_sum = 0
presentation_count = 0

while presentation_name != "Finish":
    avv_score = 0

    for _ in range(jury):
        assessment = float(input())
        avv_score += assessment
    avv_score /= jury
    print(f"{presentation_name} - {avv_score:.2f}.")
    avv_score_sum += avv_score
    presentation_count += 1

    presentation_name = input()

avv_score_sum /= presentation_count
print(f"Student's final assessment is {avv_score_sum:.2f}.")

