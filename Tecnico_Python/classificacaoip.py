ip = input("Digite um IP: ")

if ip.startswith("192.168."):
    print("Rede Privada (Classe C)")

elif ip.startswith("10."):
    print("Rede Privada (Classe A)")

elif ip.startswith("172.16."):
    print("Rede Privada (Classe B)")

else:
    print("Rede Pública")