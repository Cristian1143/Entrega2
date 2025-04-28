#llamar la libreria de python para el valor de pi
import math

#establecer la funcion matematica para conocer el area de la vagon
#se entiende que las ruedas son iguales, es decir del circunferencias de mismo radio
#valores establecidos en m (metros)

def area_vagon (radio, largo, ancho):
    area_Total = (ancho * largo) + (2 * (math.pi * radio**2))
    return area_Total
#declarar las variables de la altura, el ancho y radios de las ruedas
ancho = float(input("Ingrese el valor del ancho del vagon: "))
largo = float(input("Ingrese el valor del largo del vagon: "))
radio = float(input("Ingrese el valor del radio de las ruedas del vagon: "))
print ("El valor del area lateral del vagon corresponde a: ", area_vagon(radio,largo,ancho),"m**2")