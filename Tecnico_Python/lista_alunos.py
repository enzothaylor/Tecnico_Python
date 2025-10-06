from os import system
system('cls')

alunos_cadastro = ["Evelyn","Enzo Thaylor","Thayana","Gabriela Lima","Rafael","Thor","Pedro","Gustavo Ferraz"]
sala_2b = ["Evelyn","Enzo","Thayana","Gabriela Lima"]
sala_2d = ["Thor","Rafael"]
sala_2f = ["Gustavo Ferraz","Pedro"]

pergunta = input("Sala ou Escola: ").lower()

if pergunta == "escola":
    aluno = input("Digite o nome do aluno: ").title()
    if aluno in alunos_cadastro:
        print("Esse aluno está cadastrado na lista")
    else:
        print("Esse aluno não está cadastrado na lista")

if pergunta == "sala":
    sala = input("Digite a sala: ").lower()
    if sala == "2b":
        print(sala_2b)
    elif sala == "2d":
        print(sala_2d)
    elif sala == "2f":
        print(sala_2f)
    else:
        print("Não temos essa sala")