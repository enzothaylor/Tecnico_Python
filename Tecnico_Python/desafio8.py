from os import system
system('cls')

valor = float(input("Valor da compra: R$"))
frete = 10.00
total = valor + frete
print(f'Total com frete: R${total}')