def main():
    turno = input("Digite o turno: ")
    calculo(turno)


def calculo(turno):
    if turno == "M" or turno == "m":
        print("Bom dia")
    elif turno == "v" or turno == "V":
        print("Boa tarde")
    elif turno == "N" or turno == "n":
        print("Boa noite")
    else:
        print("Valor inválido")


main()
