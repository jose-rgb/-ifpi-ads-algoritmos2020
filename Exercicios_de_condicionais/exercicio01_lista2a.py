n1 = int(input("digite ó primeiro número: "))
n2 = int(input("digite ó segundo número: "))
n3 = int(input("digite o terceiro número: "))

if n1 == n2 == n3:
    print("todos os números são iguais, ou seja, 3 números iguais.")
elif n1 == n2:
    print(f"sómente o primeiro é o segundo são iguais, ou seja, 2 números iguais.")
elif n1 == n3:
    print(f"sómente o primeiro é o terceiro são iguais, ou seja, 2 números iguais.")
elif n2 == n3:
    print(f"sómente o segundo é terceiro são iguais, ou seja, 2 números iguais.")
else:
    print("Não tem nenhum número igual!")

