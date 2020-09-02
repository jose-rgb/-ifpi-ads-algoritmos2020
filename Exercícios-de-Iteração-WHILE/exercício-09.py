#9. Leia LimiteSuperior e LimiteInferior e escreva todos os números pares entre os limites lidos.
def main():
    lim_i = int(input('Digite o limite inferior: '))
    lim_s = int(input('Agora digite o limite superior: '))
    print(f'De {lim_i} á {lim_s}, somente os seguintes números são pares.')
    calculo(lim_s, lim_i)


def calculo(lim_s, lim_i):
    while lim_i < lim_s:
        lim_i += 1
        if lim_i % 2 == 0 and lim_i != lim_s:
            print(lim_i)


main()
