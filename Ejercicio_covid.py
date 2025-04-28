# Función para calcular el número de contagiados
def contagios(C, D):
    return C * (2 ** D)

# Declarar variables
C = int(input("Ingrese el número actual de contagiados: "))
D = int(input("Ingrese la cantidad de días: "))

# Cálculo y salida
print("El número de contagiados después de", D, "días será:", contagios(C, D))
