#22. Um fazendeiro possui fichas de controle sobre sua boiada. Cada ficha contém numero de identificação,
#nome e peso (em kg) do boi. Escreva um algoritmo que leia os dados de N fichas e ao final, escreva o
#numero de identificação e o peso do boi mais magro e do boi mais gordo.


def main():
    qtd = int(input('Quantas fichas voçê deseja inserir? '))
    mais_magro = -1
    mais_gordo = -1
    peso_magro = -1
    peso_gordo = -1

    for i in range(qtd):
        ficha = int(input('Digite á identificação da ficha: '))
        peso = float(input('Digite o peso do boi: '))
        nome = str(input('Digite o nome do boi: '))
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

        #para a primeira ficha

        if i == 0:
            mais_magro = ficha
            mais_gordo = ficha
            peso_magro = peso
            peso_gordo = peso
            nome_magro = nome
            nome_gordo = nome

        else:
            if peso < peso_magro:
                mais_magro = ficha
                peso_magro = peso
                nome_magro = nome
            if peso > peso_gordo:
                nome_gordo = nome
                mais_gordo = ficha
                peso_gordo = peso


    #Resultados
    print('-=-=-=-=-=Resultado=-=-=-=-=-')
    print(f'Identificador do boi mais magro: {mais_magro}\nPeso: {peso_magro}Kg\nNome: {nome_magro}')
    print(f'Identificador do boi mais gordo: {mais_gordo}\nPeso: {peso_gordo}Kg\nNome: {nome_gordo}')


main()
