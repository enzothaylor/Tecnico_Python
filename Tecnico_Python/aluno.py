from os import system
system('cls')

class Aluno:
    nome = ""
    nota = 0

    def mostrar_situacao(self):
        if self.nota >= 5:
            print(self.nome, "foi Aprovado/a")
        else:
            print(self.nome, "foi Reprovado/a")

a1 = Aluno()
a1.nome = "Evelyn Andrade Sena"
a1.nota = 8
a1.mostrar_situacao()

a2 = Aluno()
a2.nome = "Enzo Thaylor Carvalho Rodrigues"
a2.nota = 10
a2.mostrar_situacao()

a3 = Aluno()
a3.nome = "Diego Martins"
a3.nota = 4
a3.mostrar_situacao()

a4 = Aluno()
a4.nome = "Déborah"
a4.nota = 2
a4.mostrar_situacao()

a5 = Aluno()
a5.nome = "Tayana"
a5.nota = 6
a5.mostrar_situacao()

a6 = Aluno()
a6.nome = "Gaby"
a6.nota = 5
a6.mostrar_situacao()

a7 = Aluno()
a7.nome = "Yamil"
a7.nota = 11
a7.mostrar_situacao()