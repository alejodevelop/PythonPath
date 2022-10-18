# sistema para la entrega de 2 tipos de medicamentos en una ips

# cantidad de existencias del medicamento 1
medEx1 = int(input())
# cantidad de existencias del medicamento 2
medEx2 = int(input())

# numero de pacientes
nPacientes = 0

# numero prescripciones med1
presMed1 = 0
# numero prescripciones med2
presMed2 = 0


while medEx1 > 0 and medEx2 > 0:
    # presion Sistolica
    sisto = float(input())
    # presion Diastolica
    diasto = float(input())

    nPacientes += 1

    # deduccion de los medicamentos entregados
    if sisto < 80 and diasto < 60:
        # print("Hipotension")
        medEx2 = medEx2-5
        presMed2 += 1

    elif (sisto >= 80 and sisto < 120 and diasto >= 60 and diasto < 80):
        # print("Optima")
        continue

    elif (sisto >= 120 and sisto < 130 and diasto >= 80 and diasto < 85):
        # print("Normal")
        continue
    elif (sisto >= 130 and sisto < 140 and diasto >= 85 and diasto < 90):
        # print("Normal-Alta")
        medEx1 = medEx1 - 1
        presMed1 += 1

    elif (sisto >= 140 and sisto < 160 and diasto >= 90 and diasto < 100):
        # print("Hipertension Grado 1")
        medEx1 = medEx1 - 5
        presMed1 += 1

    elif (sisto >= 160 and sisto < 180 and diasto >= 100 and diasto < 110):
        # print("Hipertension Grado 2")
        medEx1 = medEx1 - 10
        presMed1 += 1

    elif (sisto >= 180 and diasto >= 110):
        # print("Hipertension Grado 3")
        medEx1 = medEx1 - 30
        presMed1 += 1

    elif (sisto >= 140 and diasto < 90):
        # print("Hipertension Sistolica Aislada")
        medEx1 = medEx1 - 20
        presMed1 += 1

    else:
        # print("No se puede determinar la categoria")
        continue
else:

    print(str(nPacientes))

    '''
        se imprimen la cantidad de prescripciones del medicamento 
        segun tipo y porcentaje respecto al total de medicamentos
    '''

    if presMed1 != 0:
        print(f'{presMed1} ', "{:.2f}".format(
            (100*presMed1)/nPacientes), "%")
    else:
        print(f'{presMed1} ', str(presMed1) + ".00%")

    if presMed2 != 0:
        print(f'{presMed2} ', "{:.2f}".format(
            (100*presMed2)/nPacientes), "%")
    else:
        print(f'{presMed2} ', str(presMed2) + ".00%")

    # print('medExis1: ' + str(medEx1))
    # print('medExis2: ' + str(medEx2))
