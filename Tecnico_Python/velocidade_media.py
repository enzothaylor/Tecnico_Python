from os import system
system('cls')

distancia_percorrida = float(input("Digite a distãncia percorrida (em km): "))
tempo_gasto = float(input("Digite o tempo gasto (em horas): "))
velocidade = distancia_percorrida / tempo_gasto

print(f'A velocidade média é de: {velocidade}km/h')
if velocidade >= 100:
    print("Trânsito Livre")
elif velocidade >= 60:
    print("Trânsito Moderado")
else:
    print("Trânsito Lento")