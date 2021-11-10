#Név;Neme;Részleg;Belépés;Bér
#1 feladat Hánynan dolgoznak a cégnél?
#2 feladat Hánynan dolgoznak az asztalosműhelyben?
#3.feladat Mennyi a karbantartáson dolgozók átlagfizetése?
#4.feladat Legnagyobb fizetésu dolgozó adatai?
#5.feladat Hánnyan keresnek jobban, mint 1000$ (1$=311,76Ft)
#6.feladat Hölgyek.txt-be a hölgyek és k dollárban
#7.feladat BeszerzoHolgyek.txt -> Nev, belépidő, fizut$-ban

f=open("C:\\Users\\Csongor\\Desktop\\Egyebek\\Python\\agazat\\berek.txt",encoding="utf-8")
fHolgyek=open("holgyek","w",encoding="utf-8")
fHolgyek.write("Név,Részleg;Fizetés dollár\n")

fBezHolgy=open("BeszerzoHolgyek.txt","w", encoding="utf-8")
fBezHolgy.write("Név,Belépés ideje;Fizetés\n")
fo,asztalosok, karbFo, karbFiz=0,0,0,0
maxFiz=0
maxDolg=[]
ezerDollarnalTobb=0
#sor=f.readline()
for sor in f:
    fo+=1
    sor=sor.strip('\n').split(";")
    if (sor[2]=="asztalosműhely"):
        asztalosok+=1
    if (sor[2]=="karbantartás"):
        karbFo+=1
        karbFiz+=int(sor[4])
    if maxFiz<int(sor[4]):
        maxFiz=int(sor[4])
        maxDolg=sor
    if (int(sor[4])>311.76*1000):
        ezerDollarnalTobb+=1
    if (sor[1]=="nő"):
        fizDollar=round(int(sor[4])/311.76,1)
        #fizDollar=round(fizDollar,1)
        if (fizDollar%1==0):
            fizDollar=int(fizDollar)
        fHolgyek.write(sor[0]+";"+sor[2]+";"+str(fizDollar)+"\n")
    if (sor[1]=="nő") and (sor[2]=="beszerzés"):
        fizDollar=round(int(sor[4])/311.76,1)
        if (fizDollar%1==0):
                fizDollar=int(fizDollar)
        fBezHolgy.write(sor[0]+";"+sor[3]+";"+str(fizDollar)+"\n")
    #print(sor)

f.close()
fHolgyek.close()
fBezHolgy.close()
print("1. feladat: "+str(fo)+" fő")
print("2. feladat: "+str(asztalosok)+" fő")
#print(karbFo)
#print(karbFiz)
karbAtlag=karbFiz/karbFo
if karbAtlag%1==0:
    karbAtlag=int(karbAtlag)
else:
    karbAtlag=round(karbAtlag,1)
print("3. feladat: "+str(karbAtlag)+" Ft")
print("4.feladat")
print("\tNév: "+maxDolg[0])
print("\tFizetés: "+maxDolg[4])
print("5.feladat: "+str(ezerDollarnalTobb)+" fő")