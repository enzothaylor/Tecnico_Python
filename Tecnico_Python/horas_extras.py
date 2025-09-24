valor_hora = float(input("Digite o valor por hora de trabalho: "))
horas_trabalhadas = float(input("Horas trabalhadas por mês: "))

if horas_trabalhadas > 40:
    horas_extras = horas_trabalhadas - 40
    salario_base = 40 * valor_hora
    adicional = horas_extras * valor_horas * 1.5
    salario_total = salario_base + adicional
else:
    salario_total = horas_trabalhadas * valor_hora

print(f"O salario total é R$ {salario_total}")