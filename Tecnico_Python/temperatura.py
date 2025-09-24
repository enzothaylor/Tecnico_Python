from os import system
system('cls')

# Classificar a sensação térmica com base na temperatura

temperatura = float(input("Digite a temperatura: "))

if temperatura > 30:
    print("Sensação Térmica: Está Muito Quente!")

elif temperatura >= 15:
    print("Sensação Térmica: Temperatura Agradável")

else:
    print("Sensaação Térmica: Está Frio")