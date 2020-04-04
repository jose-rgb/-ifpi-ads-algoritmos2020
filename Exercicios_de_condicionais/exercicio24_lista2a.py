def main():
    a = int(input('Qual o coeficiente A: '))
    b = int(input('Qual o coeficiente B: '))
    c = int(input('Qual o coeficiente C: '))
    if a == 0:
        print("O coeficiente A tem que ser diferente de 0, <<<Click Enter é tente novamente>>>")
        main()
    else:
        calculo(a, b, c)


def calculo(a, b, c):
    delta = (b**2) - (4 * a * c)
    primeira_raiz = ((-b) + delta**(1/2)) / 2 * a
    segunda_raiz = ((-b) - delta**(1/2)) / 2 * a
    print(f'As raizes da equação {a}x² + {b}x + {c} = 0, são x¹ = {primeira_raiz} é x² = {segunda_raiz}')


main()
