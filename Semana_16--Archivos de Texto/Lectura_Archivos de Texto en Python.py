# Crear un nuevo archivo llamado my_notes.txt
with open("my_notes.txt", "w") as file:
    # Aqui notas personales e importantes en el archivo
    file.write("Saludos Darwin Maiza.\n")
    file.write("Estudiante de Universidad Amazónica.\n")
    file.write("Gracias por su atención.\n")

# Leer el archivo my_notes.txt
with open("my_notes.txt", "r") as file:
    # Leer y mostrar el contenido línea por línea
    for line in file:
        # Se usa strip() para quitar el salto de línea al final de cada línea
        print(line.strip())