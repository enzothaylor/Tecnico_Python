from os import system
system('cls')

massa = float(input("Digite a massa do material: "))
volume = float(input("Digite o volume  do material: "))
densidade = massa / volume

print(f'A densidade do material é {densidade}kg')
if densidade >= 5:
    print("Material Muito Denso")
elif densidade >=2 :
    print("Material com Densidade Média")
else:
    print("Material com Pouca Densidade")
