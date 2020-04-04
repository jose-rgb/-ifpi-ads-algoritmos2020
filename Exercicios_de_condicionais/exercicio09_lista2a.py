def main ():
    num = int(input('Digite um número entre 0 e 100: '))
    calculo(num)

def calculo(num):
    if num > 11:
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or num % 11 == 0:
            print(f'O número {num} não é primo.')
        else:
            print(f'O número {num} é primo. ')
    elif num <= 11:
        if num == 9 or num == 1:
            print(f'O número {num} não é primo.')
        elif num % 2 == 1 or num == 2:
            print(f'O número {num} é primo')
        else:
            print(f'O número {num} não é primo')


main()
