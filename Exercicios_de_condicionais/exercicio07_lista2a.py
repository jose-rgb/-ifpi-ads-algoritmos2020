def main():
    num1 = int(input("digite o primeiro lado do triângulo: "))
    num2 = int(input("digite o segundo lado do triângulo: "))
    num3 = int(input("digite o terceiro lado do triângulo: "))
    if num1 == 0:
        print('<<<CORRIJA O PRIMEIRO LADO, POIS, NÃO EXISTE LADO DE TAMANHO IGUAL Á 0>>>.')
        main()
    elif num2 == 0:
        print('<<<CORRIJA O SEGUNDO LADO, POIS, NÃO EXISTE LADO DE TAMANHO IGUAL Á 0>>>.')
        main()
    elif num3 == 0:
        print('<<<CORRIJA O TERCEIRO LADO, POIS, NÃO EXISTE LADO DE TAMANHO IGUAL Á 0.')
        main()
    else:
        sim_nao(num1, num2, num3)


def tipo_de_triangulo(num1, num2, num3):
    if num1== num2 == num3:
        print('>>>Do tipo Equilátero, ou seja, um triângulo com três lados iguais.')
    elif num1 == num2 or num1 == num3 or num2 == num3:
        print('>>>Do tipo Isósceles, ou seja, um triângulo com dois lados iguais.')
    else:
        print('>>>Do tipo Escaleno, ou seja, com os três lados diferentes.')


def sim_nao(num1, num2, num3):
    if num1 + num2 < num3:
        print(f'>>>Os lados não formam um triângulo, pois, a soma dos dois primeiros ({num1+num2}) é menor que o terceiro lado ({num3})')
        input('<<<Aperte Enter é tente novamente com outros valores>>>')
        main()
    else:
        print(f'>>>Os lados formam um triângulo, pois a soma dos dois primeiros ({num1+num2}) é maior ou igual o terceiro lado ({num3})')
        tipo_de_triangulo(num1, num2, num3)


main()
