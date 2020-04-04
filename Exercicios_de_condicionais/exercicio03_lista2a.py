def main():
    n1 = int(input("digite ó primeiro número: "))
    n2 = int(input("digite ó segundo número: "))
    n3 = int(input("digite o terceiro número: "))
    calculo(n1, n2, n3)


def calculo(n1, n2, n3):
    if n1 > n2 > n3 or n1 > n3 >= n2:
        print("O primeiro número é o maior.")
    elif n2 > n1 > n3 or n2 > n3 > n1 or n2 > n1 == n3:
        print("O segundo número é o maior. ")
    elif  n1 == n2 > n3:
        print("O primeiro é o segundo são os maiores é são iguais.")
    elif n2 == n3 > n1:
        print('O segundo é o terceiro são os maiores é são iguais')
    elif n1 == n3 > n2:
        print("O primeiro é o terceiro são os maiores é são iguais")
    elif n3 > n1 > n2 or n3 > n2 >= n1:
        print('O terceiro  número é o maior.')
    else:
        print('Os números são iguais.')


main()

