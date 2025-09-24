from os import system
system('cls')

distancia = float(input("Qual foi a distancia percorrida em km? "))
tempo = float(input("Em quantas horas percorreu esta distancia? "))

velocidade = distancia / tempo

print(f'A velocidade média é de: {velocidade}km/h')
if velocidade > 100:
    print("O trânsito esta livre")
elif velocidade >= 60:
    print("Trânsito esta moderado")
else:
    print("O trânsito esta lento")

