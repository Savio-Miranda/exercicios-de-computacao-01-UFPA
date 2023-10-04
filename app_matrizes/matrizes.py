import random


class Matrizes():
  '''
  É uma classe que simula as diversas formas de se calcular matrizes. Alguns métodos precisam de mais de uma matriz.
  A matriz padrão é aquela passada como argumento dentro desta classe.
  '''

  def __init__(self, matriz_A: list):
    # Esta é a matriz padrão usada em diversos métodos da classe.
    self.matriz = matriz_A
    self.ordem = self._verifica_ordem(matriz_A)
  

  def _verifica_ordem(self, matriz: list):
    coluna = len(matriz[0])
    linha = 0
    for i in range(len(matriz)):
      if len(matriz[i]) != coluna:
        raise ValueError("Número de colunas incompatível dentre as linhas")
      linha += 1
    
    return (linha, coluna)


  def operar_elementos(self, n: float, operacao: str):
    """
    Realiza uma operação de n (int) aos elementos da matriz
      \nOperações disponíveis:
      - Soma = '+'
      - Multiplicação = '*' (produto escalar)
      - Potenciação = '**'
    """
    operacoes = {
      '+': lambda x: x + n,
      '*': lambda x: x * n,
      '**': lambda x: x ** n
      }
    
    for i in range(len(self.matriz)):
      for j in range(len(self.matriz[i])):
        element = self.matriz[i][j]
        self.matriz[i][j] = operacoes[operacao](element)

    return self.matriz


  def soma_de_matrizes(self, matriz_B: list):
    """
    Realiza a soma de uma matriz por outra (de mesma ordem)
    """
    ordem_B = self._verifica_ordem(matriz_B)
    if self.ordem != ordem_B:
      raise ValueError('Soma de matrizes impossível: Matrizes de ordens diferentes')

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

    for i in range(self.ordem[1]):
      for j in range(self.ordem[0]):
        linha.append(self.matriz[j][i])

      transposta.append(linha)
      linha = []

    return transposta
  

  def verificar_simetria(self):
    """
    Verifica se a matriz é simétrica
    """
    if self.matriz != self.matriz_transposta():
      return False
    
    return True
  

  def produto_de_matrizes(self, matriz_B: list):
    '''
    Produto entre duas matrizes (matriz A mxn e matriz B nxp)
    return: matriz C mxp
    '''
    ordem_B = self._verifica_ordem(matriz_B)
    if self.ordem[1] != ordem_B[0]:
      raise ValueError('Produto matricial impossível: Matrizes com colunas e linhas incompatíveis')
    
    matriz_C = []
    for i in range(self.ordem[0]):
      linha = []
      for j in range(ordem_B[1]):
        calculo = 0
        for k in range(self.ordem[1]):
          calculo += self.matriz[i][k] * matriz_B[k][j]
        linha.append(calculo)
      
      matriz_C.append(linha)
      
    return matriz_C
  

  def verifica_identidade(self):
    for i in range(len(self.matriz)):
      for j in range(len(self.matriz[i])):
        elemento = self.matriz[i][j]
        if (i == j) and (elemento != 1):
          return False
          
        elif (i != j) and (elemento != 0):
          return False
    return True

  
  def verifica_se_e_quadrada(self):
    for i in self.matriz:
      if self.ordem[0] != len(i):
        return False
    
    return True
  
  
  def gerar_matriz_quadrada(self, n: int) -> list:
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
    '''
    Dada uma matriz quadrada, retorna a soma da sua diagonal
    '''
    ordem_B = self._verifica_ordem(matriz)
    if ordem_B[0] != ordem_B[1]:
      raise ValueError('Soma de diagonal impossível: A matriz não é quadrada')
    soma = 0
    for i in range(len(matriz)):
      for j in range(len(matriz[i])):
        if i == j:
          soma += matriz[i][j]
    
    return soma
