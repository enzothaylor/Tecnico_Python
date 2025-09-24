from os import system
system('cls')

class Carro:
    marca = ""
    mdelo = ""
    ano = 0

c1 = Carro()
c1.marca = "Volkswagen"
c1.modelo = "Golf"
c1.ano = 2008

c2 = Carro()
c2.marca = "Ferrari"
c2.modelo = "Spider"
c2.ano = 2020

c3 = Carro()
c3.marca = "Toyota"
c3.modelo = "Corolla"
c3.ano = 2022

c4 = Carro()
c4.marca = "Honda"
c4.modelo = "Civic"
c4.ano = 2021

c5 = Carro()
c5.marca = "Ford"
c5.modelo = "Mustang"
c5.ano = 2023

c6 = Carro()
c6.marca = "Chevrolet"
c6.modelo = "Camaro"
c6.ano = 2020

c7 = Carro()
c7.marca = "Audi    "
c7.modelo = "A4"
c7.ano = 2023

c8 = Carro()
c8.marca = "volkswagen"
c8.modelo = "Série 3"
c8.ano = 2022

print("---- Vritines de Carros Disponíveis ----")
print(f"Marca {c1.marca}\nModelo: {c1.modelo}\nAno: {c1.ano}\n")
print(f"Marca {c2.marca}\nModelo: {c2.modelo}\nAno: {c2.ano}\n")
print(f"Marca {c3.marca}\nModelo: {c3.modelo}\nAno: {c3.ano}\n")
print(f"Marca {c4.marca}\nModelo: {c4.modelo}\nAno: {c4.ano}\n")
print(f"Marca {c5.marca}\nModelo: {c5.modelo}\nAno: {c5.ano}\n")
print(f"Marca {c6.marca}\nModelo: {c6.modelo}\nAno: {c6.ano}\n")
print(f"Marca {c7.marca}\nModelo: {c7.modelo}\nAno: {c7.ano}\n")
print(f"Marca {c8.marca}\nModelo: {c8.modelo}\nAno: {c8.ano}\n")