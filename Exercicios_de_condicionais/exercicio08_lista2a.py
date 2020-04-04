def main ():
    print(20 * '-=-')
    print('Vamos descobrir sua idade')
    print(20 * '-=-')
    dia = int(input('Que dia é hoje? '))
    mes = int(input('De qual mês? '))
    ano = int(input('Em que ano estamos? '))
    dia2 = int(input('Agora me diga o dia que você nasceu? '))
    mes2 = int(input('É em que mês? '))
    ano2 = int(input(' É o ano? '))
    calculo(dia, dia2, mes, mes2, ano, ano2)


def calculo(d1,d2,m1,m2,a1,a2):
    anos = a1 - a2
    anos_inconpleto = (a1 - a2) - 1
    if d1 >= d2 and m1 >= m2:
        print(f'Voçê tem {anos} anos de idade.')
    else:
        print(f'Voçê tem {anos_inconpleto} anos de idade.')




main()




