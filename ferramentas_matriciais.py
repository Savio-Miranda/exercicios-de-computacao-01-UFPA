import random


def criar_matriz_quadrada_aleatoria(ordem: int, teto: int):
    """
    Retorna uma matriz quadrada de ordem N com elementos aleatórios.
    ordem: ordem da matriz
    teto: o range máximo dos valores aleatórios
    """
    matriz_quadrada = []
    for i in range(ordem):
        linha = []
        for j in range(ordem):
            linha.append(random.randint(0, teto))
        
        matriz_quadrada.append(linha)
    
    return matriz_quadrada
