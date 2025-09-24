cargo = input("Digite o cargo do funcionário: ")
dia = input("Digite o dia da semana: ")


if cargo == "gerente":
    print("Acesso permitido.")
elif cargo == "analista":
    if dia in ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]:
        print("Acesso permitido.")
    else:
        print("Acesso negado.")
elif cargo == "estagiário":
    if dia in ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]:
        print("Acesso permitido.")
    else:
        print("Acesso negado.")
else:
    print("Cargo não reconhecido. Acesso negado.")
