def main():
    senha = int(input('Digite a senha: '))
    verificador(senha)


def verificador(senha):
    if senha == 1234:
        print('Seja bem vindo.')
    else:
        print('Senha incorreta \n<<tente novamente>>')
        main()


main()
