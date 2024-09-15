#Crear una matriz 3D que represente los datos de temperaturas diarias en tres ciudades

informacion_temperaturas = [
# Dimensión, se ingresan tres ciudades
    [
        [15, 22, 18, 21, 24, 23, 17],  # Semana 1
        [16, 20, 30, 14, 15, 17, 20],  # Semana 2
        [25, 30, 28, 22, 24, 26, 27]  # Semana 3
    ],  # Ciudad 1
    [
#En la tercera dimensión, semanas.
        [20, 23, 25, 18, 21, 23, 24],  # Semana 1
        [22, 25, 27, 20, 23, 25, 26]  # Semana 2
    ],  # Ciudad 2
    [
        [28, 32, 30, 26, 28, 30, 32]  # Semana 1
    ]  # Ciudad 3
]
# en otra dimensión, días de la semana
#Utilizar bucles anidados para calcular el promedio de temperaturas para una ciudad por cada una de las semanas
for ciudad in range(len(informacion_temperaturas)):
    for semana in range(len(informacion_temperaturas[ciudad])):
        acumulador = 0
        for dia in range(len(informacion_temperaturas[ciudad][semana])):  # Usamos 'dia' como índice
            acumulador += informacion_temperaturas[ciudad][semana][dia]
        promedio = acumulador / len(informacion_temperaturas[ciudad][semana])
        print(f"Ciudad {ciudad+1}, Semana {semana+1}: Promedio = {promedio:.2f}")
#Mostrar el promedio de temperaturas para cada ciudad y semana en la pantalla.

