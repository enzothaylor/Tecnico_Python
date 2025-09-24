from os import system
system('cls')

area = float(input("Qual é a area do triangulo? "))
altura = float(input("Qual é sua altura? "))
base = float(input("E sua base? "))

area = (base * altura) / 2

if area > 100:
    print("O triangulo é grande")
elif area >= 50:
    print("O triangulo é medio")
else:
    print("O triangulo é pequeno")