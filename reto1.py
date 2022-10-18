# le pido por consola dos variables al usuario

# presion sistolica
psisto = float(input())
# presion diastolica
pdiasto = float(input())

if psisto < 80 and pdiasto < 60:
    print("Hipertension Alerta Naranja")
elif psisto >= 80 and psisto < 120 and pdiasto >= 60 and pdiasto < 80:
    print("Optima Alerta Verde")
elif psisto >= 120 and psisto < 130 and pdiasto >= 80 and pdiasto < 85:
    print("Normal Alerta Verde")
elif psisto >= 130 and psisto < 140 and pdiasto >= 85 and pdiasto < 90:
    print("Normal - Alta Alerta Amarilla")
elif psisto >= 140 and psisto < 160 and pdiasto >= 90 and pdiasto < 100:
    print("Hipertension Grado 1 Alerta Naranja")
elif psisto >= 160 and psisto < 180 and pdiasto >= 100 and pdiasto < 110:
    print("Hipertension Grado 2 Alerta Roja")
elif psisto >= 180 and pdiasto >= 110:
    print("Hipertension Grado 3 Alerta Roja")
elif psisto >= 140 and pdiasto < 90:
    print("Hipertension Sistolica Aislada Alerta Naranja")
else:
    print("No se puede determinar la categoria Alerta Gris")

    #(1  - 5)
    # 2 3 4

    #[1 - 5]
    # 1 2 3 4 5
