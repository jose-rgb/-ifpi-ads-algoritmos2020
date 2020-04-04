def main():
    l1 = int(input('Digite o primeiro lado do triângulo: '))
    l2 = int(input('Digite o segundo lado do triângulo: '))
    l3 = int(input('Digite o terceiro lado do triângulo: '))
    hipotenusa = calculo(l1, l2, l3)
    catetos = calculo2(l1, l2, l3)
    print(f'À hipotenusa é o {hipotenusa},portanto, {catetos} são os catetos.')


def calculo(l1, l2, l3):
    if l1 > l2 >= l3 or l1 > l3 >= l2:
        return 'primeiro lado'

    if l2 > l1 >= l3 or l2 > l3 >= l1 :
        return 'segundo lado'

    if l3 > l2 >= l1 or l3 > l1 >= l2:
        return 'terceiro lado'


def calculo2(l1, l2, l3):
    if l1 > l2 >= l3 or l1 > l3 >= l2:
        return 'o segundo é o terceiro lado'

    if l2 > l1 >= l3 or l2 > l3 >= l1 :
        return 'o  primeiro é o terceiro lado'

    if l3 > l2 >= l1 or l3 > l1 >= l2:
        return 'o primeiro é o segundo lado'


main()

