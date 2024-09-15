def buscar_valor_en_matriz(matriz, valor_buscado):

  filas = len(matriz)
  columnas = len(matriz[0])

  for i in range(filas):
    for j in range(columnas):
      if matriz[i][j] == valor_buscado:
        return i, j

  return None

# Crear una matriz con valores
matriz = [[9, 8, 7],
          [6, 5, 4],
          [3, 2, 1]]

# Valor a buscar
valor_a_buscar = 4

# Buscar el valor en la matriz
resultado = buscar_valor_en_matriz(matriz, valor_a_buscar)

if resultado:
  fila, columna = resultado
  print(f"El Número {valor_a_buscar} que buscas en este Arreglo Multidimensional está en la posición ({fila}, {columna})")
else:
  print(f"El Número {valor_a_buscar} no se existe en el Arreglo Multidimensional.")
  #Gracias