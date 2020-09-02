#6. Escreva a tabuada dos números de 1 a 10.
def main():
    inicio = 1
    c = 0

    while inicio <= 10:
        saida = inicio * c
        print(f'{inicio} x {c} = {saida}')
        c += 1

        if c == 11:
            print("\n")
            c = 0
            inicio += 1
            saida = 0


main()
