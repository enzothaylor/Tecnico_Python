class Pessoas:
    nome = ""
    idade = 0

    def mostrarSituação(self):
        if self.idade >= 18:
            print(self.nome, "-", self.idade, "é maior de idade")
        else:
            print(self.nome, "-", self.idade, "é menor de idade")

p1 = Pessoas()
p1.nome = "Robson"
p1.idade = 10

p2 = Pessoas()
p2.nome = "claudia"
p2.idade = 45

p3 = Pessoas()
p3.nome = "janete"
p3.idade = 16

p4 = Pessoas()
p4.nome = "junior"
p4.idade = 15

p5 = Pessoas()
p5.nome = "Paniquete"
p5.idade = 18

p6 = Pessoas()
p6.nome = "Julia"
p6.idade = 14

p7 = Pessoas()
p7.nome = "Mario"
p7.idade = 5

p8 = Pessoas()
p8.nome = "Odete"
p8.idade = 17

p9 = Pessoas()
p9.nome = "Odair"
p9.idade = 15

p10 = Pessoas()
p10.nome = "Jacinto"
p10.idade = 50

# Colocar todas as pessoas dentro de uma lista
pessoas = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
# Usar um laço para verificar cada uma
for pessoa in pessoas:
    pessoa.mostrarSituação()
