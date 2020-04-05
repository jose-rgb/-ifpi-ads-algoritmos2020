def main():
    quantidade_horas = float(input("Digite quantas horas voçê trabalha no mês: "))
    valor_hora = float(input("Agora digite o quanto voçê ganha por hora: "))
    salario_bruto = valor_hora * quantidade_horas
    calculo(salario_bruto)


def calculo(salario_bruto):
     if salario_bruto <= 900:
        imposto_renda = "Isento"
        sindicato = (salario_bruto / 100) * 3
        fgts = (salario_bruto / 100) * 11
        inss = (salario_bruto / 100) * 10
        descontos = inss + sindicato
        salario_liquido = salario_bruto - descontos
        print(f"Seu salário Bruto = R${salario_bruto:.2f}\nIR = {imposto_renda}\nINSS (10%)= R${inss:.2f}"
              f"\nSindicato (3%)= R${sindicato:.2f}\n"
              f"FGTS(11%)= R${fgts:.2f}\n"
              f"Total de descontos = R${descontos:.2f}\n"
              f"Salário Liquido = R${salario_liquido:.2f}")
     elif 900 < salario_bruto <= 1500:
        imposto_renda = (salario_bruto / 100) * 5
        sindicato = (salario_bruto / 100) * 3
        fgts = (salario_bruto / 100) * 11
        inss = (salario_bruto / 100) * 10
        descontos = inss + sindicato + imposto_renda
        salario_liquido = salario_bruto - descontos
        print(f"Seu salario Bruto = R${salario_bruto:.2f}\nIR (5%)= R${imposto_renda:.2f}\nINSS (10%)= R${inss:.2f}"
              f"\nSindicato (3%)= R${sindicato:.2f}\n"
              f"FGTS(11%)= R${fgts:.2f}\n"
              f"Total de descontos = R${descontos:.2f}\n"
              f"Salário Liquido = R${salario_liquido:.2f}")
     elif 1500 < salario_bruto <= 2500:
        imposto_renda = (salario_bruto / 100) * 10
        sindicato = (salario_bruto / 100) * 3
        fgts = (salario_bruto / 100) * 11
        inss = (salario_bruto / 100) * 10
        descontos = inss + sindicato + imposto_renda
        salario_liquido = salario_bruto - descontos
        print(f"Seu salario Bruto = R${salario_bruto:.2f}\nIR (10%)= R${imposto_renda:.2f}\nINSS (10%)= R${inss:.2f}"
              f"\nSindicato (3%)= R${sindicato:.2f}\n"
              f"FGTS(11%)= R${fgts:.2f}\n"
              f"Total de descontos = R${descontos:.2f}\n"
              f"Salário Liquido = R${salario_liquido:.2f}")
     else:
        imposto_renda = (salario_bruto / 100) * 20
        sindicato = (salario_bruto / 100) * 3
        fgts = (salario_bruto / 100) * 11
        inss = (salario_bruto / 100) * 10
        descontos = inss + sindicato + imposto_renda
        salario_liquido = salario_bruto - descontos
        print(f"Seu salario Bruto = R${salario_bruto:.2f}\nIR (20%)= R${imposto_renda:.2f}\nINSS (10%)= R${inss:.2f}"
              f"\nSindicato (3%)= R${sindicato:.2f}\n"
              f"FGTS(11%)= R${fgts:.2f}\n"
              f"Total de descontos = R${descontos:.2f}\n"
              f"Salário Liquido = R${salario_liquido:.2f}")


main()
