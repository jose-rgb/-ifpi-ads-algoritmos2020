def main():
    produto_1 = float(input("Digite o preço do produto 1: "))
    produto_2 = float(input("Digite o preço do produto 2: "))
    produto_3 = float(input("Digite o preço do produto 3: "))
    calculo(produto_1, produto_2, produto_3)


def calculo(produto_1, produto_2, produto_3):
    if produto_3 >= produto_2 > produto_1 or produto_2 >= produto_3 > produto_1:
        print("O produto a ser comprado é o produto 1.")
    elif produto_3 >= produto_1 > produto_2 or produto_1 >= produto_3 > produto_2:
            print("O produto a ser comprado é o produto 2.")
    elif produto_1 >= produto_2 > produto_3 or produto_2 >= produto_1 > produto_3:
            print("O produto a ser comprado é o produto 3.")
    else:
        print("Os produtos possuem valores iguais.")


main()
