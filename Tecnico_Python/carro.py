from os import system
system('cls')

class Carro():
    marca = ""
    modelo = ""
    ano = 0
    cor = ""
    resposta = input("Quer ligar o carro (sim ou não): ")


    def buzinar(self):
        print("Bi-Bi!")
    
    def ligar(self):
        print("PHAM PHAM BRRRRRRRRRRRRRRRRR...")

    def acelerar(self):
        print("vvzzzzz ZUUUUUUUUUUUUUUUUMMMMM...")

    def freiar(self):
        print("criiiiiicchhhh")

    if resposta == "sim":
        ligar
    
c1 = Carro()
c1.marca = "Nissan"
c1.modelo = "Nissan GT3"
c1.ano = 2006
c1.cor = "Verde do Ben10"

print(f"Carro: {c1.marca} - {c1.modelo}\nAno: {c1.ano} - Cor: {c1.cor}\n")

c1.buzinar()
c1.ligar()
c1.acelerar()
c1.freiar()