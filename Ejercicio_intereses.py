# Función para calcular el pago final
def pago_prestamo(P):
    tasa = 0.03  # 3% mensual
    meses = 2
    monto_final = P * (1 + tasa) ** meses
    return monto_final

# Declarar variables
P = float(input("Ingrese la cantidad de dinero prestado: "))

# Cálculo y salida
print("El monto total a pagar después de dos meses es =", round(pago_prestamo(P), 2), "pesos")
