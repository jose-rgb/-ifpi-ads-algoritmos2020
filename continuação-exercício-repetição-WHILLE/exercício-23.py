#23. Uma determinada empresa armazena para cada funcionário uma ficha contendo o código, o número de
#horas trabalhadas e o seu nº de dependentes. Considerando que a empresa paga R$ 12,00 por hora e R$
#40,00 por dependentes e que sobre o salário são feitos descontos de 8,5% para o INSS e 5% para IR.
#Escreva um algoritmo que leia o código, número de horas trabalhadas e número de dependentes de N
#funcionários. Após a leitura de cada ficha, escreva os valores descontados para cada imposto e o salário
#líquido do funcionário.


def main():
    qtdd_funcionarios = int(input('Quantos funcionários voçê deseja Cadastrar? '))
    codigo = -1
    hrs_trabalhadas = -1
    dependentes = -1

    for i in range(qtdd_funcionarios):
        print(10 * '=-'+'Ficha'+10 * '-=')
        codigo = int(input('Qual o código do Funcionário? '))
        hrs_trabalhadas = float(input('Quantas horas trabalhadas? '))
        dependentes = int(input('Quantos Dependendes? '))
        print(22 *'=-')

        result_hrs = hrs_trabalhadas * 12
        result_dependentes = dependentes * 40
        salario = result_hrs + result_dependentes
        inss = float((salario * 85) / 1000)
        ir = float((salario * 50) / 1000)
        salario_atualizado = (salario - inss) - ir

        print(8 * '=-' + 'Contracheque' + 8 * '-=')
        print(f'Salário Bruto = R${salario:.2f}\nDesconto do INSS (8,5%) = R${inss:.2f}')
        print(f'Desconto do Imposto de Renda (5%) = R${ir:.2f}\nSalário Líquido = R${salario_atualizado}')


main()
