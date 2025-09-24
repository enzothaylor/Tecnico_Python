from os import system
system('cls')

valor = float(input("Digite o valor do produto: R$ "))

desconto = valor * 0.20
#20% = 0.20

valor_final = valor - desconto
print(f'Valor com desconto : R$ {valor_final}')