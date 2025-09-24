from os import system
system('cls')

base = float(input("Digite a base do Triângulo: "))
altura = float(input("Digite a altura do Triângulo: "))
area = (base*altura) / 2

if area >= 100:
    print("Triângulo Grande")
elif area >= 50:
    print("Triângulo Médio")
else:
    print("Triângulo Pequeno")