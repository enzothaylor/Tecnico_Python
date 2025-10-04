from os import system
system('cls')
import random

lista = ["Você Ganhou","Você Ganhou","Você Perdeu","Você Perdeu","Você Ganhou","Você Perdeu","Você Perdeu","Você Ganhou"]
random.shuffle(lista)

pergunta = int(input("Escolha um número de 0 a 7: "))
print(lista[pergunta])