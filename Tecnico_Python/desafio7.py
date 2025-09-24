from os import system
system('cls')

valor = float(input("Valor total: R$ "))
parcelas = int(input("Número de parcelas: "))
valor_parcela = valor/parcelas
print(f'Cada parcela: R$ {valor_parcela}')