# Definimos la contraseña que el sistema espera
clave_sistema = "python123"

# Primera lectura de datos (Paralelogramo en tu diagrama)
input_clave = input(">>> Ingrese su clave de acceso: ")

# Bucle de validación: Mientras sea diferente (!=)
while input_clave != clave_sistema:
    # Acción para el camino "SI" del rombo
    print("[MENSAJE]: Error de autentificación. Intente de nuevo.")
    
    # Volvemos a pedir el dato para que el bucle avance
    input_clave = input(">>> Ingrese su clave de acceso: ")

# Acción para el camino "NO" del rombo (cuando ya son iguales)
print("[SISTEMA]: Login exitoso. Bienvenido.")