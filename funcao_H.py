# 2 - Sendo H = 1 + 1/2 + 1/3 + ... 1/N. Escreva um programa que calcule o número H. O número N é fornecido pelo usuário.

def funcao_H(N: int, denominador=1, path='', H=0):
    if denominador <= N:
        return funcao_H(N, denominador + 1, path + f'1:{denominador} + ', H=1/denominador)
    
    return f'Para N = {N}:\n{path[:-3]} = {H}'

print(funcao_H(5))