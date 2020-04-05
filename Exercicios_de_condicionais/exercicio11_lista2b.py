def main():
    numero = int(input("Digite um número menor que 1000: "))
    if numero < 1000:
        calculo(numero)
    else:
        print('Número maior que 1000, tente novamente.')
        main()


def calculo(numero):
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = (numero % 100) % 10
    if centenas == 0 and dezenas == 0 and unidades != 0:
                if unidades == 1:
                    print(f"{numero} = {unidades} unidade")
                else:
                    print(f"{numero} = {unidades} unidades")

    elif centenas == 0 and dezenas != 0 and unidades == 0:
                if dezenas == 1:
                    print(f"{numero} = {dezenas} dezena")
                elif dezenas > 1:
                    print(f"{numero} = {dezenas} dezenas")

    elif centenas == 0 and dezenas != 0  and unidades != 0:
                if dezenas == 1 and unidades == 1:
                    print(f"{numero} = {dezenas} dezena e {unidades} unidade")
                elif dezenas > 1 and unidades == 1:
                    print(f"{numero} = {dezenas} dezenas e {unidades} unidade")
                elif dezenas > 1 and unidades > 1:
                    print(f"{numero} = {dezenas} dezenas e {unidades} unidades")
                elif dezenas == 1 and unidades > 1:
                    print(f"{numero} = {dezenas} dezena e {unidades} unidades")

    elif centenas != 0 and dezenas == 0 and unidades != 0:
                if centenas == 1 and unidades == 1:
                    print(f"{numero} = {centenas} centena e {unidades} unidade")
                elif centenas == 1 and unidades > 1:
                    print(f"{numero} = {centenas} centena e {unidades} unidades")
                elif centenas > 1 and unidades > 1:
                    print(f"{numero} = {centenas} centenas e {unidades} unidades")
                elif centenas > 1 and unidades == 1:
                    print(f"{numero} = {centenas} centenas e {unidades} unidade")

    elif centenas != 0 and dezenas == 0 and unidades == 0:
                if centenas == 1:
                    print(f"{numero} = {centenas} centena")
                else:
                    print(f"{numero} = {centenas} centenas")

    if centenas == 1 and dezenas == 1 and unidades == 1:
        print(f"{numero} = {centenas} centena, {dezenas} dezena e {unidades} unidade")
    elif centenas == 1 and dezenas == 1 and unidades > 1:
        print(f"{numero} = {centenas} centena, {dezenas} dezena e {unidades} unidades")
    elif centenas == 1 and dezenas > 1 and unidades == 1:
        print(f"{numero} = {centenas} centena, {dezenas} dezenas e {unidades} unidade")
    elif centenas == 1 and dezenas > 1 and unidades > 1:
        print(f"{numero} = {centenas} centena, {dezenas} dezenas e {unidades} unidades")
    elif centenas > 1 and dezenas == 1 and unidades == 1:
        print(f"{numero} = {centenas} centenas, {dezenas} dezena e {unidades} unidade")
    elif centenas > 1 and dezenas == 1 and unidades > 1:
        print(f"{numero} = {centenas} centenas, {dezenas} dezena e {unidades} unidades")
    elif centenas > 1 and dezenas > 1 and unidades == 1:
        print(f"{numero} = {centenas} centenas, {dezenas} dezenas e {unidades} unidade")
    elif centenas > 1 and dezenas > 1 and unidades > 1:
        print(f"{numero} = {centenas} centenas, {dezenas} dezenas e {unidades} unidades")
    elif centenas == 0 and dezenas != 0 and unidades == 0:
        print(f"{numero} = {dezenas} dezenas")
    else:
        print("zero")


main()

