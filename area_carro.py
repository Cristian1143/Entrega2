#llamar la libreria de python para el valor de pi
import math

#establecer la funcion matematica para conocer el area de la vagon
#se entiende que las ruedas son iguales, es decir del circunferencias de mismo radio
#valores establecidos en metros (m)

def area_circulo(radio1, radio2):
    return (math.pi * radio1 ** 2) + (math.pi * radio2 ** 2)

def area_rectangulo(ancho1,largo1,ancho2,largo2):
    return (ancho1 * largo1) + (ancho2 * largo2)

def area_lateral (radio1, radio2,ancho1,largo1,ancho2,largo2):
    return area_circulo(radio1, radio2) + area_rectangulo(ancho1, largo1, ancho2, largo2)

radio1 = float(input("Ingrese el valor del radio de la primera rueda: "))
radio2 = float(input("Ingrese el valor del radio de la segunda rueda: "))
ancho1 = float(input("Ingrese el valor del primer largo del carro: "))
ancho2 = float(input("Ingrese el valor del segundo largo del carro: "))
largo1 = float(input("Ingrese el valor del primer ancho del carro: "))
largo2 = float(input("Ingrese el valor del segundo ancho del carro: "))

# Mostrar el resultado directamente
print("El área lateral total del carro es =", area_lateral(radio1, radio2, ancho1, largo1, ancho2, largo2), "m²")