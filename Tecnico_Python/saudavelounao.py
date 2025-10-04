
csaudavel = ["salada","omelete","uva","agua","pessego"]

cnaosaudavel = ["pizza","hamburguer","batata frita","morango do amor","pastel"]

comida = input("Digite uma comida: ")

if comida in csaudavel:
    print("Essa comida é saudável.")
elif comida in cnaosaudavel:
    print("Essa comida não é saudável.")
else:
    print("Essa comida não está na lista.")
