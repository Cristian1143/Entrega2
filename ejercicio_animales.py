# Función para calcular la cantidad de carne de aves 
def carne_aves(N, M, K):
    return (N * 6) + (M * 7) + (K * 1)

# Declarar las variables
N = int(input("Ingrese el número de gallinas: "))
M = int(input("Ingrese el número de gallos: "))
K = int(input("Ingrese el número de pollitos: "))

# Imprimir la funcion del calculo
print("La cantidad total de carne en kilos es =", carne_aves(N, M, K), "kg")
