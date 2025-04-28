# Función para calcular el total a pagar
def total_compra(P, M, H):
    return (P * 300) + (M * 3300) + (H * 350)

# Función para calcular el cambio o deuda
def cambio_o_deuda(total, B):
    return B - total

# Declarar variables
P = int(input("Ingrese la cantidad de panes: "))
M = int(input("Ingrese la cantidad de bolsas de leche: "))
H = int(input("Ingrese la cantidad de huevos: "))
B = int(input("Ingrese el valor del billete entregado: "))

# Cálculo y salida
total = total_compra(P, M, H)
diferencia = cambio_o_deuda(total, B)

if diferencia >= 0:
    print("Su cambio es de:", diferencia, "pesos")
else:
    print("Debe pagar todavía:", abs(diferencia), "pesos")
