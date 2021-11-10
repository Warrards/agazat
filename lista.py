#Adatkeresés végjelig "*"
lista = []
be = input()
while (be != "*"):
    lista.append(be)
    be = input()
print(lista)

print("Keresett szöveg: ", end = "")
szoveg = input()

try:
    lista.index(szoveg)
except:
    print("A keresett szöveg nem szerepel!")
else:
    print("Igen, a szöveget tartalmazza a lista!")


#Adatkeresés végjelig "*" ismétlődés nélkül
lista = set()
print("Kérem az adatokat, végjel: '*':", end = "")
be = input()
while (be != "*"):
    lista.add(be)
    print("Kérem az adatokat, végjel: '*':", end = "")
    be = input()
print(lista)

#Adatkeresés végjelig "*"
lista = []
print("Írd be a számot: ", end = "")
be = input()
while (be != "*"):
    try:
        be = float(be)
    except:
        print("Számokat írj be, pl: 12.43: ", end = "")
    else:
        lista.append(be)
        print("Írd be a számot: ", end = "")
    be = input()
print(lista)
if (len(lista) > 0):
    atlag = sum(lista) / len(lista)
    if (atlag%1 == 0):
        atlag = int(atlag)
    else:
        atlag = round(atlag, 2)
    print("Átlag: " +str(atlag))

    print("Elvárt átlag: ", end = "")
    eA = float(input())

print("Tűrés (%): ", end = "")
tures = float(input())
tures = eA*tures/100
if ((eA-tures) <= atlag) and ((eA+tures) >= atlag):
    print("Az adatok átlaga megfelel az elvárásoknak!")
else:
    print("Az adatok hibásak!")