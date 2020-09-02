# 2. Leia N e escreva todos os números inteiros pares de 1 a N.
def main():
    n = float(input("Digite um número: "))
    inicio = 1
    c = 0
    repetidor(n, inicio, c)


def repetidor(n, inicio, c):
        while n > inicio:
            inicio += 1
            if inicio % 2 == 0:
                print(inicio)
                c += 1
        print("De 1 até {}, existem {} números pares.".format(n, c))


main()
