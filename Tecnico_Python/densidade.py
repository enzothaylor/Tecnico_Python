from os import system
system('cls')

massa = float(input("Qual é a massa do material? "))
volume = float(input("Qual é o volume do material? "))

densidade = massa / volume

if densidade > 5:
    print("Material muito denso")
elif densidade >= 2:
    print("Material com densidade media.")
else:
    ("Materia com pouca densidade.")