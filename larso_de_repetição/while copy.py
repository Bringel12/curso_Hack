
var = True
criterito_parada = 0
printar_informacoes_parada = 0

while criterito_parada != 10:
    print(criterito_parada)

    if criterito_parada == 6:
        print("seis")
        var = True

    if criterito_parada == 9:
        printar_informacoes_parada += 1

    if printar_informacoes_parada == 3:
        print("Fim do programa")
        break
    elif printar_informacoes_parada == 2:
        print("Dois")
    elif criterito_parada == 9:
        criterito_parada = 0
    else:
        criterito_parada += 1
