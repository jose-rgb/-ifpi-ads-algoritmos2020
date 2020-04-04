def main():
    print(10 * '#'+' ÍNDICE DE MASSA CORPÓREA '+10 * '#')
    alt = float(input('Qual á sua altura em metros? '))
    pes = float(input('Qual o seu peso em quilogramas? '))
    calculo(alt, pes)


def calculo(alt, pes):
    imc = pes / (alt**2)
    if imc < 25:
        print('Voçê está com peso normal.')

    if 25 < imc < 30:
        print('Voçê está obeso')

    if imc > 30:
        print('Voçê está com obesidade mórbita.')


main()