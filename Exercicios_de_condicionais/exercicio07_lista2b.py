def main():
    salario = float(input("Digite o seu salário: "))
    calculo(salario)


def calculo(salario):
    if salario <= 280:
        percentual = "20 %"
        aumento = (salario / 100) * 20
        salario_final = salario + aumento
        print(f"O salário anterior: R${salario:.2f}\nPercenutal aplicado: {percentual}\n"
              f"Valor do aumento: R${aumento:.2f}\nSalario com reajuste: R${salario_final:.2f}")
    elif 280 < salario <= 700:
        percentual = "15 %"
        aumento = (salario / 100) * 15
        salario_final = salario + aumento
        print(f"O salário anterior: R${salario:.2f}\nPercenutal aplicado: {percentual}\n"
              f"Valor do aumento: R${aumento:.2f}\nSalario com reajuste: R${salario_final:.2f}")
    elif 700 < salario <= 1500:
        percentual = "10 %"
        aumento = (salario / 100) * 10
        salario_final = salario + aumento
        print(f"O salário anterior: R${salario:.2f}\nPercenutal aplicado: {percentual}\n"
              f"Valor do aumento: R${aumento:.2f}\nSalario com reajuste: R${salario_final:.2f}")
    else:
        percentual = "5 %"
        aumento = (salario / 100) * 5
        salario_final = salario + aumento
        print(f"O salário anterior: R${salario:.2f}\nPercenutal aplicado: {percentual}\n"
              f"Valor do aumento: R${aumento:.2f}\nSalario com reajuste: R${salario_final:.2f}")


main()
