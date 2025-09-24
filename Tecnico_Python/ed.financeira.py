from os import system
system('cls')

salario = float(input("Seguindo o método 50, 15 e 35, me diga seu salario para que eu possa fazer um planejamento financeiro: "))

essenciais = salario * 0.50
prioridades = salario * 0.15
lifestyle = salario * 0.35

print(f"O planejamento financeiro ficou: ")
print(f"Essenciais: {essenciais}")
print(f"Prioridades: {prioridades}")
print(f"Lifestyle: {lifestyle}")
