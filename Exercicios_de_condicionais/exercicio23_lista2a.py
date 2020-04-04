def main():
    print('#' * 10 + ' Leitor de datas '+ 10 * '#')
    a1 = int(input('Qual o primeiro ano? '))
    m1 = int(input('Qual o primeiro mês? '))
    d1 = int(input('Qual o primeiro dia? '))
    a2 = int(input('Qual o segundo ano? '))
    m2 = int(input('Qual o segundo mês? '))
    d2 = int(input('Qual o segundo dia? '))
    calculo(a1, m1, d1, a2, m2, d2)


def calculo(a1, m1, d1, a2, m2, d2):
    if a1 == a2 and m1 == m2 and d1 > d2:
            print(f'A data {d1}/{m1}/{a1} é á mais atual.')
    elif a1 == a2 and m1 == m2 and d1 > d2:
        print(f'A data {d2}/{m2}/{a2} é á mais atual.')
    elif a1 == a2 and m1 > m2:
        print(f'A data {d1}/{m1}/{a1} é á mais atual.')
    elif a1 == a2 and m1 < m2 :
        print(f'A data {d2}/{m2}/{a2} é á mais atual.')
    elif a1 > a2:
        print(f'A data {d1}/{m1}/{a1} é á mais atual.')
    else:
        print(f'A data {d2}/{m2}/{a2} é á mais atual.')


main()
