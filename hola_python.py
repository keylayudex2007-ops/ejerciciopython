print("ingeniero senior")
print("ingresa cv")

falsas_eticas = False
experiencia = 6
domina_python = True
titulo_maestria = False
habla_ingles = True

if not falsas_eticas:
    print("candidato apto para evaluacion tecnica")
    if experiencia > 5 and domina_python:
        print("pre-seleccionado")
    elif titulo_maestria and habla_ingles:
        print("pre-seleccionado")
    else:
        print("rechazado")
else:
    print("rechazado")

print("final")