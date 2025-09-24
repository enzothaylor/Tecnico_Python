from os import system
system('cls')

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso / (altura**2)
print(f"Seu IMC é: {imc}")
