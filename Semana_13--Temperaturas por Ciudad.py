def calculo_del_promedio_temperaturas(temperaturas):

  promedios = {}
  for ciudad, semanas in temperaturas.items():
    suma_total = 0
    total_dias = 0
    for semana in semanas:
      suma_total += sum(semana)
      total_dias += len(semana)
    promedio = suma_total / total_dias
    promedios[ciudad] = promedio

  return promedios

# Datos de ciudad y temperaturas:
temperaturas = {
  "Ciudad de Quito": [[20, 22, 25, 23], [21, 19, 20, 22], [23, 24, 26, 25], [22, 21, 23, 24]],"promedio de temp."
  "Ciudad de Guayaquil": [[18, 20, 22, 21], [19, 34, 18, 20], [20, 21, 23, 22], [21, 20, 21, 22]],"promedio de temp."
  "Ciudad de Portoviejo": [[25, 27, 29, 28], [26, 24, 25, 27], [27, 28, 30, 29], [28, 27, 28, 29]]}

resultado = calculo_del_promedio_temperaturas(temperaturas)
print(resultado)
#Gracias