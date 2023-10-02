# Sistema de matrizes
from matrizes import Matrizes


matriz_A = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
matriz_B = [[1, 1, 1],[1, 1, 1], [1, 1, 1]]

base = Matrizes(matriz_A)


m1 = base.operar_elementos(1, '+')
print(f'operar elementos:\n{m1}\n')

m2 = base.soma_de_matrizes(matriz_B)
print(f'Soma de matrizes:\n{m2}\n')

m3 = base.elementos_menores_que_n(7)
print(f'Elementos menores que n:\n{m3}\n')

m4 = base.matriz_transposta()
print(f'Matriz transposta:\n{m4}\n')

m5 = base.verificar_simetria()
print(f'Verificando simetria:\n{m5}\n')

m6 = base.produto_de_matrizes(matriz_B)
print(f'Produto matricial entre matrizes A e B:\n{m6}\n')

matriz_quadrada = base.gerar_matriz_quadrada(4)
print(f'Matriz gerada:\n{matriz_quadrada}\n')

m7 = base.soma_de_diagonal(matriz_quadrada)
print(f'Soma da diagonal:\n{m7}')
