site = input("Digite o link do Site: ")

if site.startswith("https:/"):
    print("Site Seguro")
else:
    print("Site Arriscado...")