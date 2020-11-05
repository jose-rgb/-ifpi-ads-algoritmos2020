def main():

    qtdd = int(input('quantos números voçê pretende digitar? '))
    vetor = [-1] * qtdd
    c = 0
    for i in vetor:
        vetores = int(input('número a ser inserido no vetor: '))
        vetor[c] = vetores
        par(vetor)
        impar(vetor)
        positivo(vetor)
        negativo(vetor)
        c += 1

    print(f'\nVetor criado: {vetor}\ncontendo: {par(vetor)} números pares\n{impar(vetor)} ímpares')
    print(f'{positivo(vetor)} positivos\n{negativo(vetor)} negativos.')
    media(vetor)

    vetor_subst = subst(vetor)
    print(f'\nVetor substituido: {vetor_subst}')
    par(vetor_subst)
    impar(vetor_subst)
    positivo(vetor_subst)
    negativo(vetor_subst)
    print(f'contendo: {par(vetor_subst)} números pares\n{impar(vetor_subst)} ímpares')
    print(f'{positivo(vetor_subst)} positivos\n{negativo(vetor_subst)} negativos.')
    media(vetor_subst)


def par(vetor):
    par = 0
    for i in vetor:
        if i % 2 == 0:
            par += 1
      
    return par

def impar(vetor):
    impar = 0
    for i in vetor:
        if i % 2 != 0:
            impar += 1
         
    return impar

def positivo(vetor):
    positivo = 0
    for i in vetor:
        if i >  0:
            positivo += 1
         
    return positivo

def negativo(vetor):
    negativo = 0
    for i in vetor:
        if i < 0:
            negativo += 1
        
    return negativo

def subst(vetor):
    c = 0
    for i in vetor:
        if vetor[c] > 0:
            var = vetor[c] * 2
            vetor[c] = var
            c += 1

        elif vetor[c] < 0:
            var = vetor[c] / 2
            vetor[c] = var
            c += 1

    return vetor

def media(vetor):
    var = 0
    for i in vetor:
        var += i
        media = var / len(vetor)
    print(f'média dos valores: {media:.0f}') 
     

main()
