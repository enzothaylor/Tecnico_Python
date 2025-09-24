from os import system
system('cls')

class Filme:
    titulo = ""
    ano = 0
    genero = ""
    classificacao = ""

f1 = Filme()
f1.titulo = "Lilo & Stitch"
f1.ano = 2002
f1.genero = "Infantil/Comédia"
f1.classificacao = "Livre"

f2 = Filme()
f2.titulo = "Vingadores Guerra Infinita"
f2.ano = 2018
f2.genero = "Ação/Ficção Científica"
f2.classificacao = "12 Anos"

f3 = Filme()
f3.titulo = "Esquadrão Suicida"
f3.ano = 2016
f3.genero = "Ação/Fantasia"
f3.classificacao = "16 Anos"

f4 = Filme()
f4.titulo = "Pica-Pau: O Filme"
f4.ano = 2017
f4.genero = "Infantil/Comédia"
f4.classificacao = "Livre"

f5 = Filme()
f5.titulo = "Oppenheimer"
f5.ano = 2023
f5.genero = "Suspense"
f5.classificacao = "18 Anos"

f6 = Filme()
f6.titulo = "It - A Coisa"
f6.ano = 2017
f6.genero = "Terror/Mistério"
f6.classificacao = "16 Anos"

f7 = Filme()
f7.titulo = "Bob Esponja - Um Herói Fora D'Água"
f7.ano = 2015
f7.genero = "Infantil/Comédia"
f7.classificacao = "Livre"

print("Catálogo de Filmes")
print(f"Titulo: {f1.titulo}\nAno: {f1.ano}\nGênero: {f1.genero}\nClassificação: {f1.classificacao}")
print(f"Titulo: {f2.titulo}\nAno: {f2.ano}\nGênero: {f2.genero}\nClassificação: {f2.classificacao}")
print(f"Titulo: {f3.titulo}\nAno: {f3.ano}\nGênero: {f3.genero}\nClassificação: {f3.classificacao}")
print(f"Titulo: {f4.titulo}\nAno: {f4.ano}\nGênero: {f4.genero}\nClassificação: {f4.classificacao}")
print(f"Titulo: {f5.titulo}\nAno: {f5.ano}\nGênero: {f5.genero}\nClassificação: {f5.classificacao}")
print(f"Titulo: {f6.titulo}\nAno: {f6.ano}\nGênero: {f6.genero}\nClassificação: {f6.classificacao}")
print(f"Titulo: {f7.titulo}\nAno: {f7.ano}\nGênero: {f7.genero}\nClassificação: {f7.classificacao}")