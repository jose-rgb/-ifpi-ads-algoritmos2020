#11. Leia LimiteSuperior e LimiteInferior e escreva todos os números primos entre os limites lidos.
def main():
    lim_i = int(input('Digite o limite inferior: '))
    lim_s = int(input('Agora digite o limite superior: '))
    print(f'De {lim_i} á {lim_s}, somente os seguintes números são primos:')
    calculo(lim_s, lim_i)


def calculo(lim_s, lim_i):
    while lim_i < lim_s:
        if lim_i == 1 or lim_i == 2:
            lim_i += 1

        if lim_i == 2:
            print('2')
        if lim_i == 3:
            print('3')
        if lim_i == 5:
            print('5')
        if lim_i == 7:
            print('7')
        if lim_i == 11:
            print('11')
        if lim_i == 13:
            print('13')
        if lim_i == 17:
            print('17')

        if lim_i % 2 != 0 and lim_i % 3 != 0 and lim_i % 5 != 0 and lim_i % 7 != 0 and lim_i % 11 != 0 and lim_i % 13 != 0 and lim_i % 17 != 0:
            print(lim_i)
        lim_i += 1


main()
