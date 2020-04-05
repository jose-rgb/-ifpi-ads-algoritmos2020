def main():
    letra = str(input('Digite uma letra: '))
    verificador(letra)


def verificador(letra):
    if letra == "M":
        print('M-masculino')
    elif letra == "F":
        print('F-feminino')
    else:
        print('Sexo inválido')


main()
