def main():
    num = int(input('Digite um número: '))
    calculo(num)


def calculo(num):
    raiz = num**(1/2)
    dez1 = num // 100
    dez2 = num % 100
    uni = dez1 + dez2
    if raiz == uni:
        print(f'O número {num} é um quadrado perfeito')
    else:
        print(f'O número {num} não é um quadrado perfeito')


main()
