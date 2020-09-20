# 1. Leia N e escreva todos os números inteiros de 1 a N.
def main():
    n = int(input("Digite um número: "))
    repetidor(n)


def repetidor(n):
    print(f'Entre 1 é {n}, somente os seguintes números são inteiros: ')
    for i in range(2, n):
        print(i)


main()
