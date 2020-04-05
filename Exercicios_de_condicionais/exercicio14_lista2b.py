def main():
    litros = float(input("Digite a quantidade de litros: "))
    tipo = input("Digite o tipo de combustível (A-álcool, G-gasolina): ")
    resultado = calculo(litros, tipo)
    print(f"O valor á ser pago é de R${resultado:.2f}")


def calculo(litros, tipo):
    if litros <= 20 and tipo == "A":
        total = litros * 1.9
        desconto = (total / 100) * 3
        resultado = total - desconto
        return resultado

    if litros > 20 and tipo == "A":
        total = litros * 1.9
        desconto = (total / 100) * 5
        resultado = total - desconto
        return resultado

    if litros <= 20 and tipo == "G":
        total = litros * 2.5
        desconto = (total / 100) * 4
        resultado = total - desconto
        return resultado

    if litros > 20 and tipo == "G":
        total = litros * 2.5
        desconto = (total / 100) * 6
        resultado = total - desconto
        return resultado


main()
