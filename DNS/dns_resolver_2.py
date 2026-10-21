
import socket

dominio = input("Digite seu alvo: ")

with open("DNS/bruteforce.txt", "r") as arquivos:
    bruteforce = arquivos.readlines()

for nome in bruteforce:
    DNS = nome.strip("\n") + "." + dominio
    try:
        print(DNS + "; " + socket.gethostbyname(DNS))
    except socket.gaierror:
        pass
