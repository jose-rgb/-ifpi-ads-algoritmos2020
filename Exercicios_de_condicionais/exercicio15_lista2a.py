def main():
    print(7 * 'MW' + '<<<Professor 1>>>' + 7 * 'MW')
    h1 = int(input('Qual a quantidade de horas/aulas dadas pelo primeiro professor?'))
    v1 = int(input('Quanto recebe por cada hora/aula o primeiro profesor?'))
    print(7 * 'MW' + '<<<Professor 2>>>' + 7 * 'MW')
    h2 = int(input('Qual a quantidade de horas/aulas dadas pelo segundo professor?'))
    v2 = int(input('Quanto recebe por cada hora/aula o segundo profesor?'))
    calculo(h1, v1, h2, v2)


def calculo(h1, v1, h2, v2):
    prof1 = float(h1 * v1)
    prof2 = float(h2 * v2)
    if prof1 > prof2:
        print(f'O primeiro professor tem o salário maior, pois, ganha R${prof1}\nEnquanto o segundo professor ganha R${prof2}')
    elif prof2 > prof1:
        print(f'O segundo professor tem o salário maior, pois, ganha R${prof2}\nEnquanto o primeiro professor ganha R${prof1}')
    else:
        print('Os dois professores recebem o mesmo salário.')


main()
