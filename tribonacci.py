'''
Os números Tribonacci são definidos pela seguinte recursão:
    (...)
Faça um código com uma função recursiva para calcular o N-ésimo número da série de Tribonacci.
'''

def tribonacci(N: int):
    if N <= 1:
        return 0
    elif N == 2:
        return 1
    
    return tribonacci(N - 1) + tribonacci(N - 2) + tribonacci(N - 3)

print(tribonacci(7))
