'''
    Input
    Numero de sucursales
    Tipos de medicamento    
    Paciente a atender
'''

while True:

    entrada = input().split()

    numSucursales = int(entrada[0])
    tiposMedicamentos = int(entrada[1])
    numPacientes = int(entrada[2])

    if numSucursales < 1 or tiposMedicamentos < 1:
        continue
    else:
        break


'''
    Leer para las n sucursales (de 1 a n)
    Leer la cantidad de existencas de medicamentos en cada sucursal
'''
'''
    medSucursales es la lista de sucursales, cada sucursal es una posicion
    y cada posicion posee una lista de tipos de medicamentos en esa sucursal
'''

medSucursales = [None]

for i in range(numSucursales):
    medtipos = input().split()
    medSucursales.append([None])

    for j in range(tiposMedicamentos):
        medSucursales[i+1].append(int(medtipos[j]))


'''
    leer el numero de sucursal donde sera atendido, tipo de medicamento
    solicitado y numero de existencias solicitadas del medicamento,
    presion sistolica y diastolica en cada paciente. 
'''
# Lista de pacientes, cada paciente es un diccionario de datos
pacientes = []

for i in range(numPacientes):

    entrada = input().split()

    sucursal = int(entrada[0])
    medTipo = int(entrada[1])
    medCantidad = int(entrada[2])
    sisto = int(entrada[3])
    diasto = int(entrada[4])

    pacientes.append({'sucursal': sucursal,
                      'medTipo': medTipo,
                      'medCantidad': medCantidad,
                      'sisto': sisto,
                      'diasto': diasto
                      })


'''
    Validar si se programa la entrega de medicamentos
'''

'''
    medEntregados almacena los medicamentos de cada sucursal  
    separados por tipo que han sido entregados
'''

medEntregados = [None]
for i in range(numSucursales):

    medEntregados.append([0] * (tiposMedicamentos + 1))
    # Establece el valor None en la posicion 0, de cada lista de tipos dentro de cada sucursal
    medEntregados[i+1][0] = None


# idx es el indice, paciente, el diccionario que contiene los datos
for idx, paciente in enumerate(pacientes):

    sisto = paciente['sisto']
    diasto = paciente['diasto']
    medTipo = paciente['medTipo']
    medCantidad = paciente['medCantidad']
    sucursal = paciente['sucursal']

    if sucursal > 0 and sucursal <= numSucursales and medCantidad >= 0 and medTipo > 0 and medTipo <= tiposMedicamentos:

        if sisto < 80 and diasto < 60:
            # print("Hipotension")
            medEntregados[sucursal][medTipo] += medCantidad
            medSucursales[sucursal][medTipo] -= medCantidad

        elif (sisto >= 80 and sisto < 120 and diasto >= 60 and diasto < 80):
            # print("Optima")
            pass
        elif (sisto >= 120 and sisto < 130 and diasto >= 80 and diasto < 85):
            # print("Normal")
            pass
        elif (sisto >= 130 and sisto < 140 and diasto >= 85 and diasto < 90):
            # print("Normal-Alta")
            medEntregados[sucursal][medTipo] += medCantidad
            medSucursales[sucursal][medTipo] -= medCantidad

        elif (sisto >= 140 and sisto < 160 and diasto >= 90 and diasto < 100):
            # print("Hipertension Grado 1")
            medEntregados[sucursal][medTipo] += medCantidad
            medSucursales[sucursal][medTipo] -= medCantidad

        elif (sisto >= 160 and sisto < 180 and diasto >= 100 and diasto < 110):
            # print("Hipertension Grado 2")
            medEntregados[sucursal][medTipo] += medCantidad
            medSucursales[sucursal][medTipo] -= medCantidad

        elif (sisto >= 180 and diasto >= 110):
            # print("Hipertension Grado 3")
            medEntregados[sucursal][medTipo] += medCantidad
            medSucursales[sucursal][medTipo] -= medCantidad

        elif (sisto >= 140 and diasto < 90):
            # print("Hipertension Sistolica Aislada")
            medEntregados[sucursal][medTipo] += medCantidad
            medSucursales[sucursal][medTipo] -= medCantidad

        else:
            # print("No se puede determinar la categoria")
            pass

# print('pacientes: ' + str(pacientes))
# print('medSucursales: ' + str(medSucursales))
# print('medEntregados: ' + str(medEntregados))

'''
    Outputs 
    > numero Sucursal
    > numero medicamento con menos existencias disponibles despues
      de la deduccion, seguido de la cantidad de este mismo
    > numero medicamento con mas existencias disponibles despues
      de la deduccion, seguido de la cantidad de este mismo
    > cantidad minima, promedio y maxima de existencias programadas 
      para entrega  entre los tipos de medicamentos, formateado a
      2 cifras decimales, en una misma linea separado por espacio
    > el promedio de las existencias programadas para entrega de
      n pacientes en cada sucursal, si la sucursal no tiene pacientes
      el promedio debe der 0, todo formateado a dos cifras decimales
    > numero sucursal con menor cantidad de existencias programadas para 
      entrega de medicamentos tipo 1, seguido de la cantidad antes mencionada  
    > numero sucursal con mayor cantidad de existencias programadas para 
      entrega de medicamentos tipo 1, seguido de la cantidad antes mencionada  
'''


def mayor(listaMed):
    maxMed = {'indice': 1, 'medicamentos': listaMed[1]}

    for idx, e in enumerate(range(len(listaMed) - 1), 1):

        if int(maxMed['medicamentos']) < int(listaMed[idx]):

            maxMed = {
                **maxMed,
                'indice': idx,
                'medicamentos': listaMed[idx]
            }

        else:
            pass
    return maxMed


def menor(listaMed):
    minMed = {'indice': 1, 'medicamentos': listaMed[1]}

    for idx, e in enumerate(range(len(listaMed) - 1), 1):

        if int(minMed['medicamentos']) > int(listaMed[idx]):

            minMed = {
                **minMed,
                'indice': idx,
                'medicamentos': listaMed[idx]
            }

        else:
            pass
    return minMed


def sumarElementosLista(listaMed):
    sumaLista = 0
    for idx, e in enumerate(listaMed):
        if e != None:
            sumaLista += e
    return sumaLista


def pacientesXsucursal():

    pacientesXsucursal = [0] * (numSucursales + 1)

    for paciente in pacientes:
        if paciente['sucursal'] > 0 and paciente['sucursal'] <= numSucursales:
            pacientesXsucursal[paciente['sucursal']] += 1

    return pacientesXsucursal


for idx, sucursal in enumerate(medSucursales):

    if idx > 0:
        print(idx)
        # menor cantidad de existencias
        menos = menor(sucursal)
        print(f'{menos["indice"]}', f'{menos["medicamentos"]}')
        # mayor cantidad de existencias
        mas = mayor(sucursal)
        print(f'{mas["indice"]}', f'{mas["medicamentos"]}')

        # minimo, promedio, maximo entregado
        minimo = menor(medEntregados[idx])['medicamentos']
        promedio = sumarElementosLista(medEntregados[idx]) / tiposMedicamentos
        maximo = mayor(medEntregados[idx])['medicamentos']

        print("{:.2f}".format(
            minimo), "{:.2f}".format(
            promedio), "{:.2f}".format(
            maximo))

        # promedio medicamentos segun pacientes de cada sucursal
        numeroPacientes = pacientesXsucursal()[idx]

        if medEntregados[idx] != 0 and numeroPacientes != 0:
            promedio = sumarElementosLista(
                medEntregados[idx]) / numeroPacientes

        print("{:.2f}".format(
              promedio))

medsTipo1 = [None] * (numSucursales + 1)
for idx, sucursal in enumerate(medEntregados):
    if idx != 0:
        medsTipo1[idx] = sucursal[1]

# sucursal con menor cantidad de existencias programadas para entrega de medicamentos tipo 1
menorTipo1 = menor(medsTipo1)
print(f'{menorTipo1["indice"]}', f'{menorTipo1["medicamentos"]}')
# sucursal con mayor cantidad de existencias programadas para entrega de medicamentos tipo 1
mayorTipo1 = mayor(medsTipo1)
print(f'{mayorTipo1["indice"]}', f'{mayorTipo1["medicamentos"]}')
