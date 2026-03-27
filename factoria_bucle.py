# pedimos el número al usuario
n = int(input("Introduce un número para calcular su factorial: "))

# Inicializamos la variable que guardará el resultado
factoria = 1

# Bucle: Mientras n sea mayor a 0
while n > 0:
    factoria = factoria * n  # Multiplicamos el acumulado por el número actual
    n = n - 1               # Restamos 1 a n para avanzar en el bucle

# Al salir del bucle, mostramos el resultado final
print(f"El factorial es: {factoria}")