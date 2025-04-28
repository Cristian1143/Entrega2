#llamar la libreria de python para el valor de pi
import math
#establecer la funcion matematica para conocer el volumen de la figura
#valores establecidos en cm (centimentros)
def volumen_solido (radio1,h,radio2):
    volumenTotal = ((4/3) * math.pi * radio1**3) + ((1/3) * math.pi * (radio2 ** 2) * h)
    return volumenTotal
#declarar las variables de la altura, y radios de los solidos
radio1 = float(input("ingrese el valor del radio de la esfera: "))
h = float(input("ingrese el valor de la altura del cono: "))
radio2 = float(input("ingrese el valor del radio del cono: "))
print ("El valor del volumen de la esfera es= ", volumen_solido(radio1,h,radio2), "cm**3")

