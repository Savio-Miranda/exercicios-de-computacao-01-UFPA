'''
3 - Faça um código que leia um vetor de 10 valores inteiros e positivos.
A partir do vetor original, criar um segundo vetor da seguinte forma:
os elementos de índice par receberão os respectivos valores divididos por 2;
e os elementos de índice ímpar receberão os respectivos valores multiplicados por 3.
Imprima os dois vetores criados.
'''

def parity(vector: list, beyond=False):
  '''
    Returns the parity of numbers in a given vector. If you want an extra, it proceeds to divide the even by 2 and multiply the odd by 3.
      
      Parameters:
              vector (list): A list of integers
              beyond (bool): a
  
      Returns:
            result (tuple or string): string with number of even and odd numbers of vector or tuple with given new vector.
  '''
  even, odd = 0, 0
  new_vector = []
  for element in range(len(vector)):
    if vector[element] % 2 == 0:
      even += 1
      if beyond:
        new_vector.append(vector[element] // 2)

    else:
      odd += 1
      if beyond:
        new_vector.append(vector[element] * 3)

  even_odd_string = f'evens: {even}, odds: {odd}'
  result = (new_vector, even_odd_string) if beyond else even_odd_string
  return result


print(parity([4, 5, 2, 1, 2, 4, 5, 8, 3], True))