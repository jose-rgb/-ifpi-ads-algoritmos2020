#Leia N, calcule e escreva o valor de S.
#18.s = 1/N + 1/N-1 +1/N-2 ... + N/1
def main():
    num1 = int(input('Digite N: '))
    numero = 1
    resultado = 0
    num2 = num1
    while numero <= num1:
        resultado += numero / num2
        num2 = num2 - 1
        numero += 1
    print(f's = {resultado:.2f}')


main()
