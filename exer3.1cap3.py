def main():
    pergunta = input(":  ")
    right_justify(pergunta)


def right_justify(s):
    tam = len(s)
    qtdd_esp = 70 - tam
    espacos = qtdd_esp * " "
    resul = espacos + s
    print(resul)


main() 


