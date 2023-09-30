# 1 - Escreva um código que leia um vetor de 5 valores inteiros e positivos e identifique o maior valor e o menor valor do vetor


# Bônus, ainda provê a posição deles
def max_or_min(vector: list, max_is_true: bool):
    position = []
    title = ''
    if max_is_true:
        title = 'maior'
        n = max(vector)
    else:
        title = 'menor'
        n = min(vector)
    
    for index, element in enumerate(vector):
        if n == element:
            position.append(index)
    
    return {title: n, 'vector position': position}
