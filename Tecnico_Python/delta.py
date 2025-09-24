from os import system
system('cls')

# ENTRADA
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# PROCESSAMENTO
delta = b**2 - 4*a*c

# SAÍDA
print(f'O valor de Delta é: {delta}')

if delta > 0:
    print("Então a equação tem duas raízes reais")
elif delta == 0:
    print("Então a equação tem uma raiz real")
else:
    print("Então a equação não possui raízes reais")