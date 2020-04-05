def main():
    print(10 * "#" + " Interrogatório " + 10 * "#")
    r1 = input(">>>Responda somente com sim ou não.<<<\nTelefonou para a vítima ? ")
    r2 = input("Esteve no local do crime ? ")
    r3 = input("Mora perto da vítima? ")
    r4 = input("Devia para á vitima ? ")
    r5 = input("Já trabalhou com a vítima ? ")
    resultado = calculo(r1, r2, r3, r4, r5)
    print(f'A pessoa se encotra como: {resultado}')


def calculo(r1, r2, r3, r4, r5):
    soma = 0
    if r1 == 'sim':
        soma += 1

    if r2 == "sim":
        soma += 1

    if r3 == "sim":
        soma += 1

    if r4 == "sim":
        soma += 1

    if r5 == "sim":
        soma += 1

    if soma == 2:
        return "Suspeito"
    elif 2 < soma <= 4:
        return "Cúmplice"
    elif soma > 4:
        return "Assassino"
    else:
        return "Inocente"


main()
