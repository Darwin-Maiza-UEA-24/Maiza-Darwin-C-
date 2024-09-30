#Creación de diccionario llamado informacion_personal

  # con información ficticia sobre una persona

informacion_personal = {
    "Nombres": "Darwin David",
    "Edad": 42,
    "Ciudad": "Guayaquil",
    "Profesion": "Economista"
}
#Se incluyen las claves "nombre", "edad", "ciudad" y "profesion".


#Accediendo al valor asociado con la clave "ciudad" y se modifíca con ciudad diferente.
informacion_personal["Ciudad"] = "Babahoyo"

#Se agrega una nueva clave-valor al diccionario que represente la "profesion" de la persona.
informacion_personal["Profesion"] = "Ingeniero"

#Verificar Existencia de Claves:
# #Verifica si la clave "telefono" existe en el diccionario. Si no existe, agrégala con un número de teléfono ficticio.
if "telefono" not in informacion_personal:
    informacion_personal["Telefono"] = "09 9402-1646"

#Elimina la clave "edad" del diccionario, ya que esa información no es necesaria.
if "Edad" in informacion_personal:
    del informacion_personal["Edad"]

# Se imprime el diccionario resultante después de realizar todas las operaciones
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")