def main():
    opc = int(input('Digite um número entre (1,2,3): '))
    if opc == 1 or opc == 2 or opc ==3:
        num1 = int(input('Digite o segundo número: '))
        num2 = int(input('Digite o terceiro número: '))
        num3 = int(input('Digite o quarto número: '))
        calculo(opc, num1, num2, num3)
    else:
        print('Ops! Lembrando que são validos somente os números 1,2 é 3 ')
        input('<<Aperte Enter é tente novamente>>')
        main()

def calculo(opc, num1, num2, num3):
    if opc == 1:
        print(num1)
    elif opc == 2:
        print(num2)
    else:
        print(num3)


main()
