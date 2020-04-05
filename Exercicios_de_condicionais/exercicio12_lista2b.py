def main():
    num = float(input("Digite um número: "))
    calculo(num)


def calculo(num):
    if num == int(num):
        print(f"O número {num:.0f} é inteiro.")
    else:
        print(f"O número {num} é decimal.")


main()
