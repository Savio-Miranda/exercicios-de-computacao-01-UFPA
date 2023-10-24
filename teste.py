"""
SEÇÃO DE COMENTÁRIOS DA QUESTÃO:
    Ao criar uma matriz quadrada aleatória, quase nunca temos elementos
nesta matriz que sejam maiores do que a média de todos os valores. Em outras
palavras, para uma ordem muito grande de uma matriz quadrada, é improvável
haver algum elemento na matriz que seja maior do que a média de TODOS os valores.

Para testar a funcionalidade da função, adicionei uma matriz-quadrada-teste para
ser usada na função principal da questão.
"""

from ferramentas_matriciais import criar_matriz_quadrada_aleatoria


def transpor_matriz(matriz_quadrada: list):
    """
    Retorna a matriz transposta e o número de elementos acima da média
    (A média é calculada com base em TODOS os valores da matriz)
    """
    transposta = []
    n_elementos = len(matriz_quadrada) ** 2
    elementos_acima_da_media = 0
    
    media = _media_matriz(matriz_quadrada, n_elementos)
    for i in range(len(matriz_quadrada)):
        linha = []
        for j in range(len(matriz_quadrada[i])):
            linha.append(matriz_quadrada[j][i])
            if matriz_quadrada[j][i] > media:
                elementos_acima_da_media += 1
        
        transposta.append(linha)
    
    string_de_retorno = f"Transposta: {transposta}\nMedia: {media}\nElementos acima da média: {elementos_acima_da_media}"
    print(string_de_retorno)
    #return string_de_retorno # se quiser retornar a string de retorno, basta descomentar essa linha
    return transposta, elementos_acima_da_media


def _media_matriz(matriz: list, n_elementos: int):
    """
    Retorna a média de uma matriz.
    """
    media, soma = 0, 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma += sum(matriz[i])
    media = soma/n_elementos
    return media


matriz_quadrada_teste_nao_aleatoria = [[9, 1, 1, 1], [1, 1, 1, 1], [1, 1, 2, 1], [1, 1, 1, 9]]
for i in matriz_quadrada_teste_nao_aleatoria:
    print(i)
#matriz_quadrada = criar_matriz_quadrada_aleatoria(3, 3)
#transpor_matriz(matriz_quadrada)
#print(matriz_quadrada_teste_nao_aleatoria)
matriz, media = transpor_matriz(matriz_quadrada_teste_nao_aleatoria)

for i in matriz:
    print(i)