num = int(input("digite um número: "))
r1 = int(num/10)
r2 = num % 10

if r1 == r2:
    print(f'O algarismo da dezena ({r1}) é igual ao algorismo da unidade ({r2}).')
else:
    print(f'O algarismo da dezena ({r1}) é diferente do algarismo da unidade ({r2})')
