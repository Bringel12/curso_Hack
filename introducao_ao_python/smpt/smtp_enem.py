# import socket
# usuarios = ["contato", "comercial", "financeiro", "vendas", "atendiemento", "vendas", "atendimento", "root", "trial"]
# alvo = input("Alvo: ")
# for usuario in usuarios:
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.connect((alvo,25))
#     sock.recv(1024)
#     sock.send("VRFY" + usuario + "\n")
#     smtp_resultado = sock.recv(1024)
#     sock.close
#     if "252" in smtp_resultado:
#         print(usuario + "-> valido!")
#     elif "550" in smtp_resultado:
#         print(usuario +(" Usuario Invalido!"))
#     elif"503"in smtp_resultado:
#         print("servidor requer autentificação ")
#         break
#     elif "500" in smtp_resultado:
#         print("Comando VRFY não supotado pelo servidor")
#         break
#     else:
#         print("Resposta do servidor: ", smtp_resultado)

import socket

alvo = input("Servidor SMTP: ").strip()
porta = 587

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(10)

try:
    sock.connect((alvo, porta))
    print(f"[+] Conexão estabelecida com {alvo}:{porta}")

except socket.timeout:
    print("[-] Tempo limite: o servidor não respondeu.")

except OSError as erro:
    print(f"[-] Erro de conexão: {erro}")

finally:
    sock.close()