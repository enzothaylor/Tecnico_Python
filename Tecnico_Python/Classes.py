from os import system
system('cls')

# Classe chamada Pessoa

class Pessoa:
    # Atributos: Características

    nome = "" # Atributo nome
    idade = 0 # Atributo idade
    cidade = "" # Atributo cidade
    profissao = "" # Atributo profissão

# Primeiro objeto da classe Pessoa

p1 = Pessoa()
p1.nome = "Matheus Borges"
p1.idade = 17
p1.cidade = "Roma"
p1.profissao = "Estudante"

# Imprimindo Dados

print(f"Pessoa 1: {p1.nome} - {p1.idade} anos, mora em {p1.cidade} e é {p1.profissao}")

# Segundo objeto da classe Pessoa

p2 = Pessoa()
p2.nome = "Evelyn Andrade Sena"
p2.idade = 16
p2.cidade = "São Paulo"
p2.profissao = "Estudante"

# Imprimindo dados

print(f"Pessoa 2: {p2.nome} - {p2.idade} anos, mora em {p2.cidade} e é {p2.profissao}")