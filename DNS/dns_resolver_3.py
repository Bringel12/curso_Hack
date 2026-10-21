# import dns.resolver
# dominio =  input("Alvo: ")
# registros = ["AAAA", "A", "MX", "NS"]

# for registro in registros:
#     # resultado = dns.resolver.query(dominio, registros, raise_on_no_answer=False)
#     resultado = dns.resolver.resolve(dominio, registros, raise_on_no_answer=False)
#     if resultado.rrset is not None:
#         print(resultado.rrset)


import dns.resolver

dominio = input("Alvo: ")
registros = ["A", "AAAA", "MX", "NS", "TXT"]

for registro in registros:
    try:
        resultado = dns.resolver.resolve(
            dominio, registro, raise_on_no_answer=False
        )
        print(f"\n{registro}:")
        for dado in resultado:
            print(dado)
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        pass
