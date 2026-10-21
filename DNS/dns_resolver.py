import socket 
dominio = input("Alvo: ")
brunte = ["ns1", "ns2","ns3", "ns4", "www", "ftp", "intranet", "mail"]

for nome in brunte:
    DNS = nome + "." + dominio
    try:
        print (DNS + "; " + socket.gethostbyname(DNS))
    except socket.gaierror:
        pass