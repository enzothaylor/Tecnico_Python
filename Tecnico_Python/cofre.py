from os import system
system('cls')

senhacorreta = "12345"
tentativa = input("Digite a senha: d")

if tentativa == senhacorreta:
    print("Acesso Liberado!")
else:
    print("Acesso Negado!")