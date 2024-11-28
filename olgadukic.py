"""
a = 10
b = 15
print("Zbir brojeva a i b iznosi:\t", a + b)
"""
"""
a=int(input("Uneti broj a:\t"))
b=int(input("Uneti broj b:\t"))
zbir = a + b
razlika = a - b
proizvod = a * b
kolicnik = a / b
ost = a % b
cel = a // b

print(f"Zbir brojeva {a}\t i {b}\t iznosi:\t {zbir}")
print(f"Razlika  brojeva {a}\t i {b}\t iznosi:\t {razlika}")
print(f"Proizvod brojeva {a}\t i {b}\t iznosi:\t {proizvod}")
print(f"Kolicnik  brojeva {a}\t i {b}\t iznosi:\t {kolicnik}")
print(f"Ostatak pri deljenju brojeva {a}\t i {b}\t iznosi:\t {ost}")
print(f"Rezultat celobrojnog deljenja brojeva {a}\t i {b}\t iznosi:\t {cel}")
"""
"""
a=int(input("Uneti trocifren broj a:\t"))
j = a % 10
s = a // 100
d = (a//10) % 10
broj = j * 100 + d * 10 + s
print(f"Za broj {a}\t cifra jedinica je {j}\t, cifra desetica je {d}\t i cifra stotina je {s}\t dok je broj ispisan ciframa u obrnutom redosledu {broj}")
"""
"""
# ucitati brojeve a i b i ako su brojevi istog znaka odrediti zbir njihovih kvadrata, a ako su razlicitog znaka razliku njihovih kubova
import math
a=int(input("Uneti broj a:\t"))
b=int(input("Uneti broj b:\t"))
if (a > 0 and b > 0) or (a < 0 and b < 0):
    suma = math.pow (a,2) + math.pow(b,2)
    print(f"Zbir kvadrata brojeva {a}\t i {b}\t iznosi {suma}")
else:
    raz = math.pow(a,3) - math.pow(b,3)    
    print(f"Razlika kubova brojeva {a}\t i {b}\t iznosi {raz}")
"""

mesec = input("Uneti redni broj meseca u godini: ")
match mesec:
    case "1":
        print("Mesec je januar i ima 31 dan.")
    case "2":
        print("Mesec je februar i ima 28 dana.")
    case "3":
        print("Mesec je mart i ima 31 dan.")
    case "4":
        print("Mesec je april i ima 30 dana.")       
    case "5":
        print("Mesec je maj i ima 31 dan.")     
    case _:
        print("Ne postoji mesec sa datim rednim brojem")    

