'''
8 Faça uma função recursiva que receba um número inteiro positivo N e imprima
todos os números naturais de 0 até N em ordem crescente
'''

# versão 1
def contagem(n: int, k=1, soma=0, text=''):
    if k <= n:
        return contagem(n, k + 1, soma + k, text + f'{k}, ')
    return f'{text[:-1]} tal que a soma deles é...\n= {soma}'


# versão 2
def contagem2(N: int, atual=1):
    if atual <= N:
        print(atual)
        contagem2(N, atual + 1)
        return


print(contagem(10))
#print(contagem2(10))