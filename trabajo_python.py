# Control de las compuertas de la represa
nivel = float(input("Nivel de agua: "))
velocidad = input("Velocidad de llenado (alta/media/bajo): ").lower()

if nivel > 120:
    print("abrir varias compuertas y sonar alarma general")
elif nivel > 100:
    if velocidad == "alta":
        print("abrir compuerta A")
    elif velocidad == "media":
        print("abrir compuerta B")
    else:
        print("compuertas cerradas")
else:
    print("compuertas cerradas")

print("final")