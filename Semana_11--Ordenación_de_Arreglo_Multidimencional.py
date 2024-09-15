#Implementando una función que ordene una fila específica de la matriz
# en orden ascendente utilizando algoritmo buble
def bubble_sort_fila(matriz, fila_a_ordenar):

  n = len(matriz[fila_a_ordenar])
  for i in range(n):
    for j in range(0, n - i - 1):
      if matriz[fila_a_ordenar][j] > matriz[fila_a_ordenar][j + 1]:
        matriz[fila_a_ordenar][j], matriz[fila_a_ordenar][j + 1] = matriz[fila_a_ordenar][j + 1], matriz[fila_a_ordenar][j]

# Crear una matriz de ejemplo
matriz = [[3, 1, 4],
          [1, 5, 9],
          [2, 6, 7]]

# se ordena Fila (comenzando desde 0)
fila_a_ordenar = 0

print("Matriz original antes de Ordenación:")
for fila in matriz:
  print(fila)
#llamada de función de ordenación
bubble_sort_fila(matriz, fila_a_ordenar)

print("\nMatriz con la fila", fila_a_ordenar, "ordenada:")
for fila in matriz:
  print(fila)