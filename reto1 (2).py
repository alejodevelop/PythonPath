# Detección Temprana de Enfermedades no Transmisibles en un Paciente

# presion Sistolica
sisto = float(input())
# presion Diastolica
diasto = float(input())

if sisto < 80 and diasto < 60:
    print("Hipotension Alerta Naranja")

elif (sisto >= 80 and sisto < 120 and diasto >= 60 and diasto < 80):
    print("Optima Alerta Verde")

elif (sisto >= 120 and sisto < 130 and diasto >= 80 and diasto < 85):
    print("Normal Alerta Verde")

elif (sisto >= 130 and sisto < 140 and diasto >= 85 and diasto < 90):
    print("Normal - Alta Alerta Amarilla")

elif (sisto >= 140 and sisto < 160 and diasto >= 90 and diasto < 100):
    print("Hipertension Grado 1 Alerta Naranja")

elif (sisto >= 160 and sisto < 180 and diasto >= 100 and diasto < 110):
    print("Hipertension Grado 2 Alerta Roja")

elif (sisto >= 180 and diasto >= 110):
    print("Hipertension Grado 3 Alerta Roja")

elif (sisto >= 140 and diasto < 90):
    print("Hipertension Sistolica Aislada Alerta Naranja")
else:
    print("No se puede determinar la categoria Alerta Gris")
