from os import system
system('cls')

valor = float(input("Valor da Refeição: R$"))
total = valor*1.10
print(f'Total com taxa: {total}')