def main():
    print(5 * '(#)'+' Frutaria '+ 5 * '(#)')
    mor = float(input('Quantos kg de morango voçê deseja comprar ?'))
    mac = float(input('Quantos kg de maçã voçê deseja comprar ?'))
    valor_morango = calculo(mor)
    valor_maca = calculo2(mac)
    nota_fiscal(valor_morango, valor_maca, mor, mac)


def calculo(mor):
    if mor <= 5:
        total_m = mor * 2.50
        return total_m
    else:
        total_m = mor * 2.20
        return total_m


def calculo2(mac):
    if mac <= 5:
        total_ma = mac * 1.80
        return total_ma
    else:
        total_ma = mac * 1.50
        return total_ma


def nota_fiscal(valor_morango, valor_maca, mor, mac):
    print(7 * '#' + 3 * '-'+ 'Nota Fiscal' + 3 * '-' + 7 * '#')
    if valor_morango + valor_maca <= 25 and mor + mac <= 8:
        print(f'-->{mor}Kg de morango = R${valor_morango:.2f}\n-->{mac}Kg de maçã = R${valor_maca:.2f}\n-->Desconto =R$ 0.0')
        print(f'-->Total = R${valor_morango + valor_maca:.2f}')
        print(31 * '#')
    elif valor_morango + valor_maca <= 25 and mor + mac > 8:
        desconto = (10 * (valor_morango + valor_maca)) / 100
        total = (valor_morango + valor_maca) - desconto
        print(f'-->{mor}Kg de morango = R${valor_morango:.2f}\n-->{mac}Kg de maçã = R${valor_maca:.2f}\n-->Desconto =R$ {desconto:.2f}')
        print(f'-->Total = R${total:.2f}')
        print(31 * '#')
    elif valor_morango + valor_morango > 25 and mor + mac < 8:
        desconto = (10 * (valor_morango + valor_maca)) / 100
        total = (valor_morango + valor_maca) - desconto
        print(f'-->{mor}Kg de morango = R${valor_morango:.2f}\n-->{mac}Kg de maçã = R${valor_maca:.2f}\n-->Desconto =R$ {desconto:.2f}')
        print(f'-->Total = R${total:.2f}')
        print(31 * '#')
    else:
        desconto = (10 * (valor_morango + valor_maca)) / 100
        total = (valor_morango + valor_maca) - desconto
        print(f'-->{mor}Kg de morango = R${valor_morango:.2f}\n-->{mac}Kg de maçã = R${valor_maca:.2f}\n-->Desconto =R$ {desconto:.2f}')
        print(f'-->Total = R${total:.2f}')
        print(31 * '#')


main()
