"""
a=10
b=15
print("Zbir brojeva a i b iznosi:\t", a + b)
"""
"""
a=int(input("Uneti vrednost broja a:\t"))
b=int(input("Uneti vrednost broja b:\t"))
c= a + b
print("Zbir brojeva a i b iznosi:\t", c)
"""
"""
a=int(input("Uneti vrednost broja a:\t"))
b=int(input("Uneti vrednost broja b:\t"))
if b!=0:
    print("Zbir brojeva a i b iznosi:\t", a + b)
    print("Razlika brojeva a i b iznosi:\t", a - b)
    print("Proizvod brojeva a i b iznosi:\t", a * b)
    print("Kolicnik brojeva a i b iznosi:\t", a / b)
    print("Rezultat celobrojnog deljenja brojeva a i b iznosi:\t", a // b)
    print("Ostatak pri deljenju  brojeva a i b iznosi:\t", a % b)
else:
    print("Greska!")

"""
"""
a=int(input("Uneti vrednost broja a:\t"))
b=int(input("Uneti vrednost broja b:\t"))

if a>b:
    print("Veci je broj a.\t")
elif b>a:
    print("Veci je broj b.\t")
else:
    print("Brojevi su jednaki.\t") 
    
"""
import math
a = int(input("Broj a:\t"))
b = int(input("Broj b:\t"))

if (a<0 and b<0) or ( a>0 and a>0):
    suma= math.pow(a,2) + math.pow(b,2)
    print("Zbir kvadrata brojeva a i b iznosi:\t", suma)
else:
    razlika = math.pow(a,3) - math.pow (b,3) 
    print("Razlika kubova brojeva a i b iznosi:\t", razlika)

