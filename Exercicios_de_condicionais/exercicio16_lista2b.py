def main():
    print(9 *'-'+ 'Promoção de carnes Tabajara' + 9 * '-')
    print('Carnes disponiveis: Alcatra, File e Picanha.')
    tipo = str(input('#Digite somente letras minúsculas\nQual o tipo de carne voçê vai levar? '))
    qtd = float(input('Quantos kg voçê vai levar? '))
    pgm = str(input('#C-para cartão é D-para dinheiro\nVoçê vai Pagar com Cartão ou Dinheiro? '))
    valor = calculo(tipo, qtd, pgm)
    nota_fiscal(valor, tipo, pgm, qtd)


def calculo(tipo, qtd, pgm):
    if tipo == 'alcatra':
        if qtd <= 5:
            valor = qtd * 5.90
        else:
            valor = qtd * 6.80
        return valor

    if tipo == 'file':
        if qtd <= 5:
            valor = qtd * 4.90
        else:
            valor = qtd * 5.80
        return valor

    if tipo == 'picanha':
        if qtd <= 5:
            valor = qtd * 6.90
        else:
            valor = qtd * 7.80
        return valor


def nota_fiscal(valor, tipo, pgm, qtd):
    print(9 * '#' + 3 * '-' + 'Nota Fiscal' + 3 * '-' + 9 * '#')
    if pgm == 'C':
        desconto = (5 * valor) / 100
        total = valor - desconto
        print(f'#Voçê comprou:\n-->{qtd} kg de carne do tipo {tipo}\n-->desconto R$ {desconto:.2f}')
        print(f'-->Total = R$ {total:.2f}')
    else:
        print(f'#Voçê comprou:\n-->{qtd} kg de carne do tipo {tipo}\n-->desconto R$ 0.00')
        print(f'-->Total = R$ {valor:.2f}')
    print(34 * '#')


main()



