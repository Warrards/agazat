class proba:
    i = 0
    s = str("")
    def __init__(self, i, s):
        self.i=i
        self.s=s
    
    def szorzas(self, j):
        return self.i*j

    def properties(self):
        return "i: " + str(self.i) + ", s: " + self.s

print("Hello World")
r = float(2.1231423)
a = int(r)
print(type(a))
print(type(r))
print(str(a) + " " + str(r))

szorzas = a*r
print(szorzas)

mas = int(input("Pöcs: "))
print(mas)

if mas > 10 and mas <= 20:
    print("Nagyobb mint a kicsi.")
elif mas > 20:
    print("Oriási pöcsöd van-e")
else:
    print("Kicsi a pöcsöd...")
i=0
while i < 10:
    print(i)
    i += 1

dik = 1
s = str()
t = int(input("Milyen szám... : "))
while dik <= t:
    s += str(dik)
    if dik < t:
        s += "-"
    dik += 1
print(s)

p = proba(5, str("asta"))
print(p)
print(p.properties())
print(p.szorzas(10))
p.