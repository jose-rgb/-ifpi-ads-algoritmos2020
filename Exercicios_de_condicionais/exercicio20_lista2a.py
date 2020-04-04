def main ():
    ang = int(input('Digite á medida de um ângulo: '))
    calculo(ang)


def calculo(ang):
    if 0 < ang <= 90:
        print('O ângulo está no primeiro quadrante.')
    elif  90 < ang <= 180:
        print('O ângulo está no segundo quadrante.')
    elif 180 < ang <= 270:
        print('O ângulo está no terceiro quadrante.')
    elif 270 < ang <= 360:
        print('O ângulo está no quarto quadrante.')
    else:
        print('Ângulo inválido, é aceito apenas ângulos entre 0° é 360°.')


main()