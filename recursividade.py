# contagem recursiva de k até n
def contagem(n: int, k=1, soma=0, text=''):
    if k <= n:
        return contagem(n, k + 1, soma + k, text + f'{k}, ')
    return f'{text[:-1]} tal que a soma deles é...\n= {soma}'

print(contagem(10))

def contagem2(N: int, atual=1):
    if atual <= N:
        print(atual)
        contagem2(N, atual + 1)
        return
    
#print(contagem2(10))