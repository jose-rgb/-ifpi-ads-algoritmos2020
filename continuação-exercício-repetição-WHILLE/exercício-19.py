#19. s = 1/N + N-1/2 + 3/N-2 ... + N/1
def main():
    n = int(input('Digite N: '))
    numero = 1
    resultado = 0
    while n >= 1:
        if numero % 2 != 0:
            resultado += numero / n
        else:
            resultado -= n / numero

        n -= 1
        numero += 1

    print(f'A soma é {resultado:.2f}')


main()
