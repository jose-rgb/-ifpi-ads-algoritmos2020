def main():
    val = int(input('Digite o primeiro valor: '))
    val2 = int(input('Digite o segundo valor: '))
    ope = int(input('digite 1 para Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão: '))
    calculo(val, val2, ope)


def calculo(val, val2, ope):
    if ope == 1:
        print(f'À adição dos números é igual á: {val + val2}')
    elif ope == 2:
        print(f'À subtração dos números é igual á: {val - val2} ')
    elif ope == 3:
        print(f'À multiplicação dos números é igual á: {val * val2} ')
    elif ope == 4:
        print(f'À divisão dos números é igual á: {val / val2}')
    else:
        print('OPERADOR INVÁLIDO! SÓ É PERMITIDO: 1 para Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão ')


main()
