# Sistema de matrizes
from matrizes import Matrizes


matriz_teste = [[-2, 1, 7], [1, 0, 2], [7, 3, 8]]
matriz_teste_2 = [[4, 5, 1], [-4, 2, 5], [3, -5, 9]]
base = Matrizes(matriz_teste) 


m1 = base.matriz_somada_n(1)
print(f'Matriz somada com n:\n{m1}\n')

m2 = base.soma_de_matrizes(matriz_teste_2)
print(f'Soma de matrizes:\n{m2}\n')

m3 = base.verificar_simetria()
print(f'Verificando simetria:\n{m3}\n')

m4 = base.matriz_transposta()
print(f'Matriz transposta:\n{m4}\n')

m5 = base.elementos_menores_que_n(5)
print(f'Elementos menores que n:\n{m5}\n')

m6 = base.produto_escalar(matriz_teste_2)
print(f'Produto escalar entre a matriz e a matriz B:\n{m6}\n')

matriz_gerada = base.gerar_matriz_nxn(4)
print(f'Matriz gerada:\n{matriz_gerada}\n')

m7 = base.soma_de_diagonal(matriz_gerada)
print(f'Soma da diagonal:\n{m7}\n')
