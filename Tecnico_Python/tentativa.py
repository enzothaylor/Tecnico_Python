# Solicita a entrada do usuário
num1 = float(input("Digite o primeiro número: "))
operador = input("Digite a operação (+, -, *, /, **, %): ")
num2 = float(input("Digite o segundo número: "))

# Verifica qual operação foi escolhida
if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    if num2 != 0:  # Evita divisão por zero
        resultado = num1 / num2
    else:
        resultado = "Erro! Divisão por zero."
elif operador == "**":
    resultado = num1 ** num2  # Potência
elif operador == "%":
    if num2 != 0:  # Evita erro de divisão por zero
        resultado = num1 % num2  # Módulo (resto da divisão)
    else:
        resultado = "Erro! Divisão por zero."
else:
    resultado = "Operação inválida!"

# Exibe o resultado
print("Resultado:", resultado)