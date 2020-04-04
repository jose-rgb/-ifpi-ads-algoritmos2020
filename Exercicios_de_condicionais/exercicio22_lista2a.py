def main():
    print('#' * 10 + ' Calculador de duração de jogos '+ 10 * '#')
    h1 = int(input('Digite o horário que começou o jogo.\n horas? '))
    m1 = int(input('minutos? '))
    h2 = int(input('Agora digite o horário que terminou o jogo.\n horas? '))
    m2 = int(input('minutos? '))
    horas = calculo_horas(h1, h2)
    minutos = calculo_minutos(m1, m2)
    print(f'O jogo durou {horas} horas é {minutos} minutos.')


def calculo_horas(h1, h2):
    if h2 < h1:
        return (24 - h1) + h2

    if h2 > h1:
        return h2 - h1

    if h1 == h2:
        return 24


def calculo_minutos(m1, m2):
    minutos = m1 + m2
    if minutos > 60:
        return ( minutos - 60) + m2
    else:
        return m1 + m2


main()
