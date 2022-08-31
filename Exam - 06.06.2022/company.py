ime_na_kompaniq = str(input())
broi_bileti_vuzrastni = int(input()) #15
broi_detski_bileti = int(input()) #5
netna_cena_za_vuzrasten = float(input()) #120
taksa_obslujvane = float(input()) #40
detski_bilet = netna_cena_za_vuzrasten * 0.3
cena_na_vuzrasten_s_taksa = netna_cena_za_vuzrasten + taksa_obslujvane
detski_bilet_s_taksa_obslujvane = detski_bilet + taksa_obslujvane

obshta_cena = (cena_na_vuzrasten_s_taksa * broi_bileti_vuzrastni) + \
              (detski_bilet_s_taksa_obslujvane * broi_detski_bileti)

pechalba = obshta_cena * 0.2
print(f"The profit of your agency from {ime_na_kompaniq} tickets is {pechalba:.2f} lv.")





