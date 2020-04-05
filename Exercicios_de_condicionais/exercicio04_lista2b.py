def main():
    nota_1 = float(input("Digite a primeira nota: "))
    nota_2 = float(input("Digite a segunda nota: "))
    calculo(nota_1, nota_2)


def calculo(nota_1, nota_2):
    media = (nota_1 + nota_2) / 2
    if media == 10:
        print("Aprovado com distinção")
    elif media >= 7 and media < 10:
        print("Aprovado")
    elif media < 7:
        print("Reprovado")
    else:
        print("Digite notas válidas")

main()