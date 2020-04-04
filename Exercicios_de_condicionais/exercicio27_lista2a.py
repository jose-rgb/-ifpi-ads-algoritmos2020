def main():
    print(20 * '-=-')
    print('Vamos descobrir sua idade')
    print(20 * '-=-')
    dia2 = int(input('Que dia é hoje? '))
    mes2 = int(input('De qual mês? '))
    ano2 = int(input('Em que ano estamos? '))
    dia = int(input('Agora me diga o dia que você nasceu? '))
    mes = int(input('É em que mês? '))
    ano = int(input(' É o ano? '))
    anos = calculo_ano(mes, mes2, ano, ano2)
    meses = calculo_meses(mes, mes2)
    dias = calculo_dias(dia, dia2, mes, mes2)
    print(f'Voçê tem {anos} anos e {meses} meses é {dias} dias')


def calculo_ano( mes, mes2, ano, ano2):
    anos = ano2 - ano
    ano_inconpleto = (ano2 - ano) - 1
    if mes2 >= mes:
        return anos
    else:
        return ano_inconpleto


def calculo_meses(mes, mes2):
    if mes2 > mes:
        meses = mes2 - mes
        return meses
    elif mes2 < mes:
        meses = mes2 - 1
        return meses
    else:
        return 0


def calculo_dias(dia, dia2, mes, mes2):
    if dia2 < dia and mes2 == mes:
        return dia2
    elif dia2 > dia and mes2 == mes:
        dias = dia2 - dia
        return dias
    elif dia2 < dia and mes2 <= mes:
        return dia2
    elif dia2 > dia and mes2 >= mes:
        return dia2
    else:
        return dia2


main()


