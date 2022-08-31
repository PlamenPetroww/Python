broi_dogrami = int(input())
vid_na_dogramata = str(input())
nachin_na_poluchavane = str(input())
obshto = 0
edinichna_cena = 0


if vid_na_dogramata == "90X130":
    edinichna_cena = 110
    if broi_dogrami >= 30:
        edinichna_cena *= 0.95
    elif broi_dogrami >= 60:
        edinichna_cena *= 0.92

if vid_na_dogramata == "100X150":
    edinichna_cena = 140
    if broi_dogrami >= 40 and broi_dogrami < 80:
        edinichna_cena *= 0.94
    elif broi_dogrami >= 80:
        edinichna_cena *= 0.9

if vid_na_dogramata == "130X180":
    edinichna_cena = 190
    if broi_dogrami >= 20 and broi_dogrami < 50:
        edinichna_cena *= 0.93
    elif broi_dogrami >= 50:
        edinichna_cena *= 0.88

if vid_na_dogramata == "200X300":
    edinichna_cena = 250
    if broi_dogrami >= 25 and broi_dogrami < 50:
        edinichna_cena *= 0.91
    elif broi_dogrami >= 50:
        edinichna_cena *= 86

obshto = broi_dogrami * edinichna_cena



if broi_dogrami > 99 and nachin_na_poluchavane == "Without delivery":
    obshto = edinichna_cena * broi_dogrami
elif broi_dogrami > 99 and nachin_na_poluchavane == "With delivery":
    obshto = edinichna_cena * broi_dogrami
    obshto += 60
    obshto *= 0.96



if broi_dogrami < 10:
    print("Invalid Order")

print(f"{obshto:.2f} BGN")