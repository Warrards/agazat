hofok = []
print("Írd be a mérésed eredményeit: (pl.: 21.68), végjel '0': ", end = "")
fok = float(input())
while (fok != 0):
    hofok.append(fok)
    print("Írd be a mérésed eredményeit: (pl.: 21.68), végjel '0': ", end = "")
    fok = float(input())
print("Írd be az elvárt átlag hőmérsékletet: ", end = "")
elvart_fok = float(input())
print("Írd be a megengedett eltérést százalékban: ", end = "")
szazalek = float(input())

szazalek = elvart_fok * (szazalek / 100)
atlag = sum(hofok)/len(hofok)

if (elvart_fok - szazalek) <= atlag and (elvart_fok + szazalek) >= atlag:
    print("Jók vagyunk!")
else:
    print("Mindenki meg fog fagyni!")
