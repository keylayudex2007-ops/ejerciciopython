# Mi programa para el control de acceso
sensor = input("¿El sensor está activo? (si/no): ")
identificacion = int(input("Digita tu identificación: "))
traje = input("¿Traes el traje de protección? (si/no): ")

id_autorizado = 1001993

if sensor == "si":
    print("acceso denegado por seguridad")
else:
    if identificacion == id_autorizado and traje == "si":
        print("acceso autorizado")
    else:
        print("equipo incompleto")

print("final")