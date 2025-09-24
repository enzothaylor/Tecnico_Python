from os import system
system('cls')

n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
n3 = float(input("DIgite sua terceira nota: "))
n4 = float(input("Digite sua quarta nota: "))

media = (n1 + n2 + n3 + n4)/4
print(f'Sua média final é {media}')

if media >= 5:
    print("Aprovado(a)")
else:
    print("Reprovado(a)")