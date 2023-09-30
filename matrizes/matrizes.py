import random


class Matrizes():

  def __init__(self, matriz: list):
    self.matriz = matriz

  def matriz_somada_n(self, n: int):
    """
    Realiza a soma de n (int) aos elementos da matriz 
    """
    for i in range(len(self.matriz)):
      for j in range(len(self.matriz[i])):
        self.matriz[i][j] += n

    return self.matriz

  def soma_de_matrizes(self, matriz_B: list):
    """
    Realiza a soma de uma matriz por outra
    """
    for i in range(len(self.matriz)):
      for j in range(len(self.matriz[i])):
        self.matriz[i][j] += matriz_B[i][j]

    return self.matriz

  def elementos_menores_que_n(self, n: int):
    """
    Dada um número n (int), retorna os elementos da matriz que sejam menores que n
    """
    count = 0
    for i in range(len(self.matriz)):
      for j in range(len(self.matriz[i])):
        if self.matriz[i][j] < n:
          count += 1

    return count

  def matriz_transposta(self):
    """
    Realiza a transposta da matriz
    """
    transposta = []
    linha = []

    for i in range(len(self.matriz)):
      for j in range(len(self.matriz[i])):
        linha.append(self.matriz[j][i])

      transposta.append(linha)
      linha = []

    return transposta

  def verificar_simetria(self):
    """
    Verifica se a matriz é simétrica
    """
    simetria = True
    if self.matriz != self.matriz_transposta():
      simetria = False
      return simetria

    return simetria
  
  def produto_escalar(self, matriz_B: list):
    soma = 0
    string_de_retorno = ''
    for linha in range(len(self.matriz)):
        for elemento in range(len(self.matriz[linha])):
          soma += self.matriz[linha][elemento] * matriz_B[linha][elemento]
          string_de_retorno += f'({self.matriz[linha]} * {matriz_B[linha]}) + '
    
    return (soma, string_de_retorno[:-3])

  
  def gerar_matriz_nxn(self, n: int) -> list:
    """
    Gera uma matriz nxn
    """
    matriz = []
    for i in range(n):
        line = []
        for j in range(n):
            line.append(random.uniform(-5, 5).__round__(2))

        matriz.append(line)

    return matriz


  def soma_de_diagonal(self, matriz: list):
    soma = 0
    for i in range(len(matriz)):
      for j in range(len(matriz[i])):
        if i == j:
          soma += matriz[i][j]
    return soma
