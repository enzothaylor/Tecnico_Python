from os import system
system('cls')

valor = float(input("Digite o valor do produto: R$ "))
desconto = 0.10

valorFinal = valor - (valor*desconto)
print(f"Valor com desconto: R$ {valorFinal}")