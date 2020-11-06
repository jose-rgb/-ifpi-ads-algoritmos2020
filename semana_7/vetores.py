def main():
    lista = []
    menu()
    option = int(input('\nEscolha uma opção: '))
    analise_option(option, lista)


def menu():
    print('****** Brincando com listas ******\n1-Inserir Valores')
    print('2-Mostrar Valores\n3-Mostrar valor de acordo com a posição')
    print('4-Remover valor\n5-atualizar valor\n6-sair')


def analise_option(option, lista):
    while True:
        if option == 1:
            inseridos = inserir(lista)
            print(f'\nLista Criada: {inseridos}')
            break
        elif option == 2:
            mostrar_valores(lista)
            break
        elif option == 3:
            mostrar_position(lista)
            break
        elif option == 4:
            remover(lista)
            break
        elif option == 5:
            atualizar(lista)
            break
        elif option == 6:
            print('saindo.....')
            break
        else:
            print('Digite uma opção válida.')    
    input('<<Enter>> para continuar')
    menu()
    option = int(input('\nEscolha uma opção: '))
    analise_option(option, lista)



def inserir(lista):
    qtdd = int(input('quantos valores voçê deseja inserir? '))
    for i in range(qtdd):
        valor = int(input('valor a ser inserido: '))
        lista.append(valor)
    return lista

def mostrar_valores(lista):
    if lista == []:
        print('lista vazia: []\nTente inserir valores na lista\n')
    else:
        print(lista)
 
 
def mostrar_position(lista):
    position = int(input('Digite o índice do valor que deseja: '))
    c = 0
    for i in lista:
        if position == c:
            print(F'valor: {i}')
        c += 1

    if position > len(lista) - 1:
        print(F'Lista não contém esse índice, pois, só possui {len(lista)} valores.')
        print('Sendo que, o primeiro valor está no índice 0.')
    

def remover(lista):
    valor = int(input('Digite o valor a ser removido da lista: '))
    var = valor in lista
    if  var == True:
        lista.remove(valor)
        print(f'{valor} removido da lista.')
    else:
        print('valor não existe na lista')

def atualizar(lista):
    valor = int(input('qual valor voçê deseja alterar? '))
    alterado = int(input('digite o valor que irá substituir: '))
    var = valor in lista
    if var == True:
        c = 0
        for i in lista:
            if i == valor:
                lista[c] = alterado
            c += 1
        print('valor alterado com sucesso')
    else:
        print(f'{valor} não existe na lista')
    

main()
