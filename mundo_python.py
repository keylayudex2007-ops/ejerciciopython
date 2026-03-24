# Programa de ventas y descuentos
tipo_cliente = input("Tipo de cliente (VIP/otro): ")
total_compra = float(input("Digite total de la compra: "))

if tipo_cliente == "VIP":
    if total_compra > 500000:
        descuento = total_compra * 0.30
    else:
        descuento = total_compra * 0.10
    print(f"El valor con descuento es = {total_compra - descuento}")
elif total_compra > 500000:
    descuento = total_compra * 0.20
    print(f"Total con descuento: {total_compra - descuento}")
else:
    print("No aplica descuento")
    
print("final")