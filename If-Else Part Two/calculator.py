broi_hora = int(input())
season = str(input())
total = 0

if broi_hora <= 5 and season == "spring":
    total = 50 * broi_hora
if broi_hora <= 5 and season == "summer":
    total = (48.5 * 0.85) * broi_hora
if broi_hora <= 5 and season == "autumn":
    total = 60 * broi_hora
if broi_hora <= 5 and season == "winter":
    total = (86 * 1.08) * broi_hora
if broi_hora > 5 and season == "spring":
    total = 48 * broi_hora
if broi_hora > 5 and season == "summer":
    total = (45 * 0.85) * broi_hora
if broi_hora > 5 and season == "autumn":
    total = 49.5 * broi_hora
if broi_hora > 5 and season == "winter":
    total = (85 * 1.08) * broi_hora
print(f"{total:.2f} leva.")




