'''
Dados dois vetores A e B de mesmo tamanho, calcule o produto escalar desses
vetores, que é a soma dos produtos dos elementos correspondentes:
A[0]*B[0] + A[1]*B[1] + ... + A[n]*B[n].
Exemplo de Entrada: A = [1, 2, 3], B = [4, 5, 6]
Exemplo de Saída: 32 (1*4 + 2*5 + 3*6)
'''

def produto_escalar(A: list, B: list):
    soma = 0
    string_de_retorno = ''
    for elemento in range(len(A)):
        soma += A[elemento] * B[elemento]
        string_de_retorno += f'({A[elemento]} * {B[elemento]}) + '
    
    return (soma, string_de_retorno[:-3])

print(produto_escalar([1, 2, 3], [4, 5, 6]))