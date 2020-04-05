def main():
    nota1 = int(input('Digite a primeira nota: '))
    nota2 = int(input('Insira a segunda nota: '))
    calculo(nota1,nota2)


def calculo(nota1,nota2):
    media = (nota1 + nota2) / 2
    if media >= 9:
        print (f'Sua média é {media}')
        print(f'Sua nota é A')
        print(f'Você foi aprovado. ')

    if 9> media >= 7.5:
        print (f'Sua média é {media}')
        print(f'Sua nota é B')
        print(f'Você foi aprovado. ')

    if 7.5 > media >= 6:
        print (f'Sua média é {media}')
        print(f'Sua nota é C')
        print(f'Você foi aprovado. ')

    if 5 >= media >= 4:
        print (f'Sua média é {media}')
        print(f'Sua nota é D')
        print(f'Você foi reprovado. ')

    if media <= 4:
        print (f'Sua média é {media}')
        print(f'Sua nota é E')
        print(f'Você foi reprovado. ')


main()
