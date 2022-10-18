# sistema para la distribucion de medicamentos en diferentes sucursales


'''
     recoleccion numero de sucursales y pacientes
'''

while True:

    # recibo una entrada de tipo string
    # split me retorna una lista conformada por cada elemento separado por un espacio dentro del string
    sucursalesPacientes = input().split()

    # cantidad de sucursales
    numSucursales = int(sucursalesPacientes[0])
    # cantidad de pacientes a atender
    numPacientes = int(sucursalesPacientes[1])

    if numSucursales < 1:
        continue
    else:
        break


# medSucursales, lista que contiene la cantidad de medicamentos en cada sucursal
# dado a que no puede haber 0 sucursales, se inicializa con el valor 0
medSucursales = [None]


# lista paciente contendra varios diccionarios de datos que tendran los valores por cada persona
'''
    {
        numero de sucursal a la que asiste,
        presionDiastolica,
        presionSistolica
    }
    
'''
pacientes = []


'''
     recoleccion de datos acerca de inventario de medicamentos por cada sucursal
'''

while True:

    if int(len(medSucursales)) <= numSucursales:
        medicamentos = int(
            input())
        # se valida que las existencias no sean inferiores a 1
        if medicamentos < 1:
            continue
        else:
            medSucursales.append(medicamentos)
    else:
        break

# Se crea una lista que almacenará los medicamentos entregados según sucursal
# la lista se inicializa con valores vacios
'''
    se le suma 1 a numSucursales por que la lista debe tener una
    posicion de mas, la 0 que posee 0 de valor dado a que no se usa
'''
medEntregados = [0] * (numSucursales + 1)


'''
     recoleccion de datos respecto a sucursal y
     presion sistolica y diastolica de cada paciente
'''

for i in range(numPacientes):

    datosPaciente = input().split()

    sucursal = datosPaciente[0]
    sisto = datosPaciente[1]
    diasto = datosPaciente[2]

    pacientes.append({'sucursal': sucursal, 'sisto': sisto, 'diasto': diasto})

# print(pacientes)


'''
    Entrega de medicamentos a pacientes
    Se descontaran de su respectiva sucursal
    de haber datos erroneos, no se descuenta
'''

# idx es el indice, paciente, el diccionario que contiene los datos
for idx, paciente in enumerate(pacientes, 1):
    sucursal = int(paciente['sucursal'])
    sisto = int(paciente['sisto'])
    diasto = int(paciente['diasto'])
    # print(paciente)
    # print(idx)

    if sucursal <= int(len(medSucursales)) and sucursal > 0:
        if sisto < 80 and diasto < 60:
            # print("Hipotension")
            medSucursales[sucursal] -= 5
            medEntregados[sucursal] += 5
        elif (sisto >= 80 and sisto < 120 and diasto >= 60 and diasto < 80):
            # print("Optima")
            continue
        elif (sisto >= 120 and sisto < 130 and diasto >= 80 and diasto < 85):
            # print("Normal")
            continue
        elif (sisto >= 130 and sisto < 140 and diasto >= 85 and diasto < 90):
            # print("Normal-Alta")
            medSucursales[sucursal] -= 2
            medEntregados[sucursal] += 2
        elif (sisto >= 140 and sisto < 160 and diasto >= 90 and diasto < 100):
            # print("Hipertension Grado 1")
            medSucursales[sucursal] -= 5
            medEntregados[sucursal] += 5
        elif (sisto >= 160 and sisto < 180 and diasto >= 100 and diasto < 110):
            # print("Hipertension Grado 2")
            medSucursales[sucursal] -= 10
            medEntregados[sucursal] += 10
        elif (sisto >= 180 and diasto >= 110):
            # print("Hipertension Grado 3")
            medSucursales[sucursal] -= 30
            medEntregados[sucursal] += 30
        elif (sisto >= 140 and diasto < 90):
            # print("Hipertension Sistolica Aislada")
            medSucursales[sucursal] -= 20
            medEntregados[sucursal] += 20
        else:
            # print("No se puede determinar la categoria")
            continue
    # print(nMedSucursales)

'''
     Outputs:
'''

'''
     Numero de la sucursal con la menor cantidad de existencias
     cantidad existencias

     Numero de la sucursal con la mayor cantidad de existencias
     cantidad existencias

     Nota: de haber 2 sucursales con el mismo min y max, debe mostrarse
     segun su numero, ejm: sucursal 1 vs sucursal 2, mostrar sucursal 1
'''


# posicion 'indice' almacena la posicion de la sucursal en la lista
# posicion 'medicamentos' almacena la cantidad de medicamentos
minMedSucursal = {'indice': 1, 'medicamentos': medSucursales[1]}
maxMedSucursal = {'indice': 1, 'medicamentos': medSucursales[1]}

for idx, elemento in enumerate(medSucursales, 2):
    if idx <= numSucursales:
        if minMedSucursal['medicamentos'] > medSucursales[idx]:
            # ** hace una copia del diccionario anterios, su fucion es similar a la del spread operator de JS
            # para modificar el diccionario, tambien se puede usar su metodo update que recibe otro diccionario
            minMedSucursal = {
                **minMedSucursal,
                'indice': idx,
                'medicamentos': medSucursales[idx]
            }
        else:
            pass

        if maxMedSucursal['medicamentos'] < medSucursales[idx]:
            # ** hace una copia del diccionario anterios, su fucion es similar a la del spread operator de JS
            # para modificar el diccionario, tambien se puede usar su metodo update que recibe otro diccionario
            maxMedSucursal = {
                **maxMedSucursal,
                'indice': idx,
                'medicamentos': medSucursales[idx]
            }
        else:
            pass
    else:
        break


print(f"{minMedSucursal['indice']} {minMedSucursal['medicamentos']}")
print(f"{maxMedSucursal['indice']} {maxMedSucursal['medicamentos']}")


'''
     imprimir proporcion porcentual medicamentos a entregar respecto al total de existencias 
     formato: cada sucursal en orden ascendente y linea separada
     numero Sucursal seguido de, 2 cifras decimales y separado por espacio 
'''

# medSucursales
# medEntregados

for idx, enumerate in enumerate(medSucursales, 1):

    if idx <= numSucursales:

        totalMedicamentos = medSucursales[idx] + medEntregados[idx]
        descontados = medEntregados[idx]
        # se saca porcentaje de los medicamentos entregados respecto a las existencias previas

        porcentaje = (descontados*100)/totalMedicamentos
        print(f'{idx}', "{:.2f}".format(
            porcentaje), "%")
