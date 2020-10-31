import dbm
import pickle


def main():
    
    
    #inicializar
    banco = dbm.open('smartphones', 'w')
    smart_rec = pickle.loads(banco['str'])

    mostrar_disponiveis(smart_rec)  

    #buscar por marca
    print( 25 * '#'+"-Smartphones-"+ 25 * '#')
    marca = str(input("Qual a Marca de smartphone voçê procura? ").upper())
    
    #primeiro_menu
    page_landing()
    option = int(input('Escolha uma opção: '))
    list_or_quit(option, marca, banco)
    
    #selecionar
    select(banco)
    
    
def list_or_quit(option, marca, banco):
    
    if option != 0 and option != 1:
        input("Selecione uma opção válida. <<Enter>>")
        page_landing()
        option = int(input('Escolha uma opção: '))
        list_or_quit(option, marca, banco)

    elif option == 1:
        listing(marca, banco)


    elif option == 0:
        print('saindo.....')
        input('<<Enter>> para rodar a aplicação')
        main()
    
    banco.close()


    
#listar_smartphones
def listing(marca, banco):
    print('\nSmartphones dísponiveis: ')

    smart_rec = pickle.loads(banco['str'])

    c = 0
    for i in smart_rec:
        lista = smart_rec[c]
        c += 1

        if lista['marca'] == marca:
            print(lista['marca'], lista['nome'])
        
       
    banco.close()
   


def select(banco):
    banco = dbm.open('smartphones', 'w')
    cell = input('\nDigite o nome do smartphone que voçê deseja selecionar: \nexemplo: Iphone12\n>>>').upper()   
    smart_rec = pickle.loads(banco['str'])
    option2 = int(input('\nVoçê deseja:\n1-Ver detalhes.\n2-Remover.\n3-Editar.\n4-Adicionar um novo smartphone\n>>>'))


    if option2 == 1:
       c = 0
       for i in smart_rec:
           lista = smart_rec[c]
           c += 1
           if lista['nome'] == cell:
               print(i)

    if option2 == 2:
       c = 0
       for i in smart_rec:
           lista = smart_rec[c]
           if lista['nome'] == cell:
              
               remove = smart_rec.pop(c)
               banco['str'] = pickle.dumps(smart_rec)
               print(f'{remove} foi removido com sucesso.')
           c += 1
               
    if option2 == 3:
       c = 0
       for i in smart_rec:
           lista = smart_rec[c]
           c += 1
           if lista['nome'] == cell:
               print(f">>nome atual: {lista['nome']}")
               print(f">>marca atual: {lista['marca']}")
               print(f">>tela atual: {lista['tela']}")
               print(f">>preço atual: {lista['preco']}")
               
               
               print('\nAgora digite as especificações que deseja mudar: ')
               print('obs: caso não queira mudar alguma configuração, digite a atual.')
            
               name_edt = input('Novo nome: ').upper()
               marca_edt = input('Nova marca: ').upper()
               tela_edt = str(input('Nova tela: ')).upper()
               preco_edt = str(input('Novo preço: ')).upper()
               
               

               smartphone_edt = {'nome': name_edt, 'marca': marca_edt, 'tela': tela_edt, 'preco': preco_edt}
               
               smart_rec.pop(c-1)
               banco['str'] = pickle.dumps(smart_rec)
               smart_rec.insert(c, smartphone_edt)
               banco['str'] = pickle.dumps(smart_rec)
               print(f'Smartphone editado com sucesso..Novos dados:\n{smartphone_edt}')

    if option2 == 4:
       c = 0
       for i in smart_rec:
           lista = smart_rec[c]
           c += 1
           if lista['nome'] == cell:
               name_new = input('nome do novo smartphone: ').upper()
               marca_new = input('marca do novo smartphone: ').upper()
               tela_new = str(input('tela do novo smartphone: ')).upper()
               preco_new = str(input('preço do novo smartphone: ')).upper()
               print('Smartphone cadastrado com sucesso...')
               
               

               smartphone_new = {'nome': name_new, 'marca': marca_new, 'tela': tela_new, 'preco': preco_new}
               smart_rec.append(smartphone_new)
               banco['str'] = pickle.dumps(smart_rec)

               banco.close()




def mostrar_disponiveis(smart_rec):

    marcas = []
    for smartphone in smart_rec:
        marca = smartphone['marca']
        marcas.append(marca)
    
    print(60 * '#'+'\nNo momento só estas marcas estão dísponíveis no nosso estoque:')
    print(sorted(set(marcas)))
    print('')

def page_landing():
    print( "###########################t-Opções-############################\n"
     "0-sair.\n"
     "1-Listar smartphones de acordo com a marca.\n")
   

main()