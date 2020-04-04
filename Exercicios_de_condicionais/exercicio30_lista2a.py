def main():
    num = int(input('Digite um número entre 1000 e 9999: '))
    if 1000 <= num <= 9999:
        calculo(num)
    else:
        print(f'O número {num} não está entre 1000 e 9999, Tente novamente ')
        main()


def calculo(num):
    primeiros = num // 100
    segundos = num % 100
    soma = primeiros + segundos
    if soma**2 == num:
        print(f' {num} obedece a regra: {num} -> dividindo = {primeiros} e {segundos} -> somando temos {soma}->{soma}² ={num}.')
    else:
        print(f' {num} Não obedece a regra.')


main()

