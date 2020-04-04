def main():
    n1 = float(input('Qual á primeira nota? '))
    n2 = float(input('Qual á segunda nota? '))
    resultado(n1, n2)


def resultado(n1, n2):
    media = (n1 + n2)/ 2
    if media >= 7:
        print('PARABÉNS, Voçê foi aprovado!')
    else:
        print('Infelizmente voçê não atingiu a média')
        final(media)


def final(media):
    n3 = float(input('Qual á sua nota na prova final?'))
    if media + n3 >= 5:
        print('PARABÉNS, Voçê foi aprovado na exame final.')
    else:
        print('Infelizmente voçê foi novamente reprovado, pois, não atingiu á média no exame final.')


main()
