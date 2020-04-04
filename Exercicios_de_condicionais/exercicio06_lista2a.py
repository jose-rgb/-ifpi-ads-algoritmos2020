def main():
    num1 = int(input("digite o primeiro ângulo: "))
    num2 = int(input("digite o segundo ângulo: "))
    num3 = int(input("digite o terceiro ângulo: "))
    if num1 == 0:
        print('<<<CORRIJA O PRIMEIRO ÂNGULO, POIS, NÃO EXISTE ÂNGULO IGUAL Á 0>>>.')
    elif num2 == 0:
        print('<<<CORRIJA O SEGUNDO ÂNGULO, POIS, NÃO EXISTE ÂNGULO IGUAL Á 0>>>.')
    elif num3 == 0:
        print('<<<CORRIJA O TERCEIRO ÂNGULO, POIS, NÃO EXISTE ÂNGULO IGUAL Á 0.')
    else:
        sim_não(num1, num2, num3)
        acutangulo(num1, num2, num3)


def sim_não(num1, num2, num3):
    if num1 + num2 + num3 == 180:
        print(f'>>>Os ângulos internos {num1}°, {num2}° é {num3}° formam um triângulo')
    else:
        print(f'>>>Os ângulos internos {num1}°, {num2}° é {num3}° Não formam um triângulo')
        input('Se deseja consultar outros ângulos, Aperte <<Enter>>')
        main()


def acutangulo3(num3):
    if num3 < 90:
        print('>>>Do tipo acutângulo, pois, os três ângulos são menores que 90°.')
    elif num3 ==90:
        print(f'>>>É como o terceiro ângulo é igual á 90°, Formam um triângulo Retângulo.')
        input('Se deseja consultar outros ângulos, Aperte <<Enter>>')
        main()
    elif num3 > 90:
        print('>>>É como o terceiro ângulo é maior que 90°, Formam um triângulo Obtusângulo.')
        input('Se deseja consultar outros ângulos, Aperte  <<Enter>>')
        main()
    else:
        print(f'>>> Porém,como o terceiro ângulo ({num3}°) é maior ou igual 90°, Não formam um triângulo Acutângulo.')


def acutangulo2(num2,num3):
    if num2 < 90:
        acutangulo3(num3)
    elif num2 ==90:
        print('>>>É como o segundo ângulo  é igual á 90°, Formam um triângulo Retângulo.')
        input('Se deseja consultar outros ângulos, Aperte  <<Enter>>')
        main()
    elif num2 > 90:
        print('>>>É como o segundo ângulo é maior que 90°, Formam um triângulo Obtusângulo.')
        input('Se deseja consultar outros ângulos, Aperte  <<Enter>>')
        main()
    else:
        print(f'>>> Porém,como o segundo ângulo ({num2}°) é maior ou igual 90°, Não formam um triângulo Acutângulo.')


def acutangulo(num1, num2, num3):
    if num1 < 90:
        acutangulo2(num2, num3)
    elif num1 ==90:
        print('>>>É como o primeiro ângulo é igual á 90°, Formam um triângulo Retângulo.')
        input('Se deseja consultar outros ângulos, Aperte em <<Enter>>')
        main()
    elif num1 > 90:
        print('>>>É como o primeiro ângulo é maior que 90°, Formam um triângulo Obtusângulo.')
        input('Se deseja consultar outros ângulos, Aperte  <<Enter>>')
        main()
    else:
        print(f">>>Porém, Não formam um triângulo Acutângulo, pois o primeiro ângulo ({num1}°) é maior ou igual á 90°.")


main()

