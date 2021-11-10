import terbeli
import math

test = terbeli.kup(5,10)
print("Felszín: " + str(test.felszin()))
print("Térfogat: " + str(test.terfogat()))

sik_idom = terbeli.rombusz(4,math.pi/2)
print("Kerület: " + str(sik_idom.kerulet()))
print("Terület: " + str(sik_idom.terulet()))
print("Eljárás: " + str(sik_idom.eljaras()))
