class animais:
    espécie = ""
    idade = 0
    cor = ""

    def miar2(self):
        print("MEOWMEOW")
    def miar(self):
        print("MEOW MEOW MEOW")
    def miar3(self):
        print("MEOW MEOW MEOWWW")

a1 = animais()
a1.espécie = "Scottish fold"
a1.idade = 0
a1.cor = "cinza"

a2 = animais()
a2.espécie = "Ragdoll"
a2.idade = 0
a2.cor = "branco"

a3 = animais()
a3.espécie = "Chartreux"
a3.idade = 0
a3.cor = "cinza escuro"

a4 = animais()
a4.espécie = "Norueguês da floresta"
a4.idade = 0
a4.cor = "laranja com branco"

a5 = animais()
a5.espécie = "Azul russo"
a5.idade = 0
a5.cor = "cinzinha"

print("Raça: ", a1.espécie, "-", "Cor: ", a1.cor, "-", "Idade: ", a1.idade, "meses.")
a1.miar2()
print("Raça: ", a2.espécie, "-", "Cor: ", a2.cor, "-", "Idade: ", a2.idade, "meses.")
a1.miar()
print("Raça: ", a3.espécie, "-", "Cor: ", a3.cor, "-", "Idade: ", a3.idade, "meses.")
a1.miar3()
print("Raça: ", a4.espécie, "-", "Cor: ", a4.cor, "-", "Idade: ", a4.idade, "meses.")
a1.miar2()
print("Raça: ", a5.espécie, "-", "Cor: ", a5.cor, "-", "Idade: ", a5.idade, "meses.")
a1.miar()