# 7. Leia um número N, some todos os números inteiros entre 1 e N e escreva o resultado obtido.
def main():
    n = int(input("Digite um número: "))
    inicio = 2
    c = 0
    escrever_n(n, inicio, c)
    soma_n(n)


def escrever_n(n, inicio, c):
    print(f'>>Os números inteiros entre 1 e {n} são: ')
    while n > inicio:
        inicio += 1
        c += 1
        print(inicio - 1)


def soma_n(n):
    soma = 0
    i = 1
    while i < n:
        soma += i
        i += 1
    print(f'>>É a soma deles é igual á: {soma - 1}')


main()
