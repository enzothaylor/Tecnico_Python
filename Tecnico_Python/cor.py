from os import system
system('cls')

cores = ["vermelho","verde","azul"]

cor = input("Digite uma cor: ")

if cor in cores:
    print("Sim, a cor está na lista.")
else:
    print("A cor não está na  lista.")

