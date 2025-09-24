class Jogo:
    nome = ""
    genero = ""
    jogadores = 0

    def iniciar(self):
        print("iniciando:", self.nome)
    def jogar(self):
        print("jogando:", self.nome, "com", self.jogadores)

j1 = Jogo()
j1.nome = "Minecraft"
j1.genero = "Sandbox"
j1.jogadores = "30"

j2 = Jogo()
j2.nome = "GTA V"
j2.genero = "Ação"
j2.jogadores = 30

print("jogo: ", j1.nome, "-", j1.genero)
j1.iniciar()
j1.jogar()

print("jogo: ", j2.nome, "-", j2.genero)
j2.iniciar()
j2.jogar()