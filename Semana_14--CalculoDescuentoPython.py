# Creando una función llamada Calcular_descuento y toma de dos parámetros:
# 1.- El monto o suma total de la compra
# 2.- El valor predeterminado de 10% de descuento

def calcular_descuento(Suma_total, porcentaje_descuento=10):  # por defecto 10%
# Calcula el descuento revisando la suma total de la compra y el porcentaje de descuento

    descuento = (Suma_total * porcentaje_descuento) / 100
    return descuento
#Retorna:
    #float: El monto del descuento calculado.

if __name__ == "__main__":
    while True:
        try:
            Suma_total = float(input("Ingrese el monto total de la compra: "))
            porcentaje_descuento_input = input("Ingrese el porcentaje de descuento (o deje en blanco para usar el predeterminado 10%): ")

            # Comprobando si se dejó en blanco para usar el valor predeterminado
            if porcentaje_descuento_input == "":
                porcentaje_descuento = 10
            else:
                porcentaje_descuento = float(porcentaje_descuento_input)

            descuento = calcular_descuento(Suma_total, porcentaje_descuento)
            print(f"El descuento para un monto de {Suma_total} con un descuento del {porcentaje_descuento}% es: {descuento}")

        except ValueError:
            print("Por favor, ingrese valores numéricos válidos.")

        continuar = input("¿Desea realizar otro cálculo? (s/n): ")
        if continuar.lower() != 's':
            break