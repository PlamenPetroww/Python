player = ""
golove = 0
vkarani = 0
naiDobriq = 0
ishave = True
player = input()

while player != "END":

    golove = int(input())

    if golove > vkarani:
        vkarani = golove
        naiDobriq = player
    if golove >= 10:
        print(f"{player} is the best player!")
        print(f"He has scored {golove} goals and made a hat-trick !!!")
        ishave = False
        break
    player = input()

    if player == "END":
        player = naiDobriq
        if golove >= 3:
            print(f"{player} is the best player!")
            print(f"He has scored {golove} goals and made a hat-trick !!!")
            break
        elif golove <= 3:
            print(f"{player} is the best player!")
            print(f"He has scored {golove} goals.")
            break