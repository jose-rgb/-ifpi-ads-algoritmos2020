num1 = int(input("digite o primeiro número: "))
num2 = int(input("digite o segundo número: "))
num3 = int(input("digite o terceiro número: "))

if num1 > num2 > num3:
    print(f'Os números em ordem crescente fica: {num3},{num2},{num1}')
elif num1 > num3 > num2:
    print(f'Os números em ordem crescente fica: {num2},{num3},{num1}')
elif num2 > num3 > num1:
    print(f'Os números em ordem crescente fica: {num1},{num3},{num2}')
elif num2 > num1 > num3:
    print(f'Os números em ordem crescente fica: {num3},{num1},{num2}')
elif num3 > num1 > num2:
    print(f'Os números em ordem crescente fica: {num2},{num1},{num3}')
else:
    print(f'Os números em ordem crescente fica: {num1},{num2},{num3}')
    

