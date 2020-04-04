def main():
    print(20 * '-=-')
    print('Verificador de datas.')
    print(20 * '-=-')
    dia = int(input('digite o dia: '))
    mes = int(input('digite o mês: '))
    ano = int(input('digite o ano: '))
    calculo(dia, mes, ano)


def calculo(dia, mes, ano):
    if 30 > dia >= 1:
        if 12 > mes >= 1:
            if 2020 > ano >= 1582:   # 1582, data de promulgação do calendario gregoriano
                print(f'A data {dia}/{mes}/{ano} é valida.')
    else:
        print(f'A data {dia}/{mes}/{ano} não é valida.')


main()
