def main():
    print('MW' * 17)
    print('Digite apenas números diferentes!')
    print('MW' *17)
    n1 = int(input("digite ó primeiro número: "))
    n2 = int(input("digite ó segundo número: "))
    n3 = int(input("digite o terceiro número: "))
    n4 = int(input("digite o quarto número: "))
    n5 = int(input("digite o quinto número: "))
    calculo_maior(n1, n2, n3)
    calculo_maior2(n4, n5)
#calcula é escreve o maior número
    maior_numero = calculo_maior(n1, n2, n3)
    maior_numero2 = calculo_maior2(n4, n5)
    retornar_maior(maior_numero, maior_numero2)
#calcula é escreve o menor número
    calculo_menor(n1, n2, n3)
    calculo_menor2(n4, n5)
    menor = calculo_menor(n1,n2,n3)
    menor2 = calculo_menor2(n4, n5)
    retornar_menor(menor, menor2)


def calculo_maior(n1, n2, n3,):
    if n1 > n2 > n3 or n1 > n3 > n2:
        return n1
    elif n2 > n1 > n3 or n2 > n3 > n1:
        return n2
    else:
        return n3


def calculo_maior2(n4, n5):
    if n4 > n5:
        return n4
    else:
        return n5


def retornar_maior(maior_numero,maior_numero2):
    if maior_numero > maior_numero2:
        print(f'O maior número é {maior_numero}.')
    else:
        print(f'O maior número é {maior_numero2}.')


def calculo_menor(n1, n2, n3):
    if n1 < n2 < n3 or n1 < n3 < n2:
        return n1
    elif n2 < n1 < n3 or n2 < n3 <n1:
        return n2
    else:
        return n3


def calculo_menor2(n4, n5):
    if n4 < n5:
        return n4
    else:
        return n5


def retornar_menor(menor, menor2):
    if menor < menor2:
        print(f'É o menor número é {menor}.')
    else:
        print(f'É o menor número é {menor2}.')


main()
