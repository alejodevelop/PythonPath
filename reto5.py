import csv
import math

'''
    1. Leer informacion del archivo data.csv y almacenarla en un diccionario
'''

branchs = input()
branchs = branchs.split()

# convierto todos los elementos de la lista en enteros
branchs = [int(br) for br in branchs]
# ordeno los elementos de la lista de menor a mayor
branchs = sorted(branchs, reverse=False)


# Dicdata = {
#     'first_name': 0,
#     'last_name': 1,
#     'gender': 2,
#     'city_name': 3,
#     'department_name': 4,
#     'id_branch': 5,
#     'medicine_type': 6,
#     'medicine_quantity': 7,
#     'systolic_pressure': 8,
#     'diastolic_pressure': 9,
# }


'''
    data es una lista de diccionarios con los datos del archivo data.csv
    organizados en filas y columnas como en el excel
'''
data = []

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)

    for fila in reader:
        data.append(fila)


'''
    findElementByKey recibe:
    data, la lista que contenga diccionarios a recorrer
    whereToFind, el indice del diccionario  a encontrar
    whatToFind, el valor a encontrar en el diccionario
    return, el diccionario con los valores buscados
'''


def findElementByKey(data, keyToFind, valueToFind):

    for dt in data:
        if dt[keyToFind] == valueToFind:
            return dt
    else:
        return {
            'first_name': None,
            'last_name': None,
            'gender': None,
            'city_name': None,
            'department_name': None,
            'id_branch': None,
            'medicine_type': None,
            'medicine_quantity': None,
            'systolic_pressure': None,
            'diastolic_pressure': None,
        }


# def countElementsByKey(data, wichValuesToAdd):
#     values = 0
#     for dt in data:
#         if dt[wichValuesToAdd]:
#             values += 1
#     else:
#         return values

'''
    findElementsByKey recibe:
    data 'args[0]', la lista que contenga diccionarios a recorrer
    whereToFind 'args[1]', el indice del diccionario a encontrar
    whatToFind (opcional) 'args[2]', el valor a encontrar en el diccionario
    return, una lista con los diccionarios buscados
'''


def findElementsByKey(*args):

    elements = []
    data = args[0]
    whereToFind = args[1]
    try:
        whatToFind = args[2]
    except:
        whatToFind = None

    for dt in data:

        if whatToFind != None:
            if dt[whereToFind] == whatToFind:
                elements.append(dt)
        else:

            elements.append(dt)
    else:
        return elements


'''
    getDictionaryValues recibe:
    data, la lista que contenga diccionarios a recorrer
    key, la posicion del diccionario en donde obtener el valor
'''


def getDictionaryValues(data, key):

    values = []

    for dt in data:
        values.append(dt[key])
    else:
        return values


'''
    calculateAverage recibe:
    data, lista de datos
    return, promedio de los datos dentro de la lista data
'''


def calculateAverage(data):

    sumTotalElements = 0
    numberOfElements = len(data)

    for dt in data:
        sumTotalElements += float(dt)

    return sumTotalElements / numberOfElements

    '''
        calculateStandardDeviation recibe:
        data, conjunto de datos
        average, es el promedio de los datos que contiene data
        isDataSampleOfWholePopulation, boolean que determina si data corresponde
        al total de la poblacion o a una muestra del total de la poblacion
        return, un float con la desviacion estandar 
    '''


def calculateStandardDeviation(data, average, isDataSampleOfWholePopulation=False):
    '''
        Formula:
        > para una poblacion completa
            DE = √ Σ |x - y|^2 / N
        > para una muestra de la poblacion completa
            DE = √ Σ |x - y|^2 / (N - 1)
        Donde:
            DE = desviacion estandar
            x = un valor de un conjunto de datos
            y = media del conjunto de datos
            N = numero de datos en el conjunto
    '''

    x = 0
    y = float(average)
    n = len(data)

    for dt in data:
        x += math.pow((float(dt) - y), 2)

    if isDataSampleOfWholePopulation:
        de = math.sqrt((x/(n - 1)))
    else:
        de = math.sqrt((x/n))

    return de


'''
    convertListData recibe:
    data, lista a convertir
    returnType, tipo de dato al que se convertira la lista
    return, una lista nueva con los tipos de dato pasado por argumento
'''


def convertListData(data, returnType):

    newList = []
    returnType = type(returnType)

    if returnType == type(1):
        newList = [int(dt) for dt in data]
    if returnType == type(1.1):
        newList = [float(dt) for dt in data]
    if returnType == type("str"):
        newList = [str(dt) for dt in data]

    return newList


'''
    medsDeliveryValidation recibe:
    patients, es la lista de la cual se sacaran las presiones 
    sistolicas y diastolicas, para verificar la presion de la
    persona y dar un diasnostico
    return, una lista con los diccionarios de pacientes aptos para la entrega,
    asi como una key mas para cada paciente apto llamada diagnostico
'''


def medsDeliveryValidation(patients):

    peopleSuitableForDelivery = []

    for p in patients:

        sisto = float(p['systolic_pressure'])
        diasto = float(p['diastolic_pressure'])

        if sisto < 80 and diasto < 60:
            # print("Hipotension")
            p = {
                **p,
                'diagnostic': "hipotension"
            }
            peopleSuitableForDelivery.append(p)

        elif (sisto >= 80 and sisto < 120 and diasto >= 60 and diasto < 80):
            # print("Optima")
            p = {
                **p,
                'diagnostic': "optima"
            }

            pass
        elif (sisto >= 120 and sisto < 130 and diasto >= 80 and diasto < 85):
            # print("Normal")
            p = {
                **p,
                'diagnostic': "normal"
            }

            pass
        elif (sisto >= 130 and sisto < 140 and diasto >= 85 and diasto < 90):
            # print("Normal-Alta")
            p = {
                **p,
                'diagnostic': "normal-alta"
            }
            peopleSuitableForDelivery.append(p)

        elif (sisto >= 140 and sisto < 160 and diasto >= 90 and diasto < 100):
            # print("Hipertension Grado 1")
            p = {
                **p,
                'diagnostic': "hipertension grado 1"
            }
            peopleSuitableForDelivery.append(p)

        elif (sisto >= 160 and sisto < 180 and diasto >= 100 and diasto < 110):
            # print("Hipertension Grado 2")
            p = {
                **p,
                'diagnostic': "hipertension grado 2"
            }
            peopleSuitableForDelivery.append(p)

        elif (sisto >= 180 and diasto >= 110):
            # print("Hipertension Grado 3")
            p = {
                **p,
                'diagnostic': "hipertension grado 3"
            }
            peopleSuitableForDelivery.append(p)

        elif (sisto >= 140 and diasto < 90):
            # print("Hipertension Sistolica Aislada")
            p = {
                **p,
                'diagnostic': "hipertension sistolica aislada"
            }
            peopleSuitableForDelivery.append(p)

        else:
            # print("No se puede determinar la categoria")
            pass

    return peopleSuitableForDelivery


'''
    minimun recibe:
    data, la lista de datos  llena de diccionarios a analizar
    key, el nombre de la propiedad en la cual buscar los datos en los diccionarios
    return, el diccionario con el valor minimo de la propiedad buscada
'''


def minimun(data, key):

    values = getDictionaryValues(data, key)

    values = convertListData(values, 1)

    minValue = str(min(values))

    minimun = findElementByKey(data, key, minValue)

    return minimun


'''
    maximun recibe:
    data, la lista de datos  llena de diccionarios a analizar
    key, el nombre de la propiedad en la cual buscar los datos en los diccionarios
    return, el diccionario con el valor maximo de la propiedad buscada
'''


def maximun(data, key):

    values = getDictionaryValues(data, key)

    values = convertListData(values, 1)

    maxValue = str(max(values))

    maximun = findElementByKey(data, key, maxValue)

    return maximun


'''
    Outputs
'''

for branch in branchs:

    '''
        la siguiente linea convierte el numero almacenado en esta poscion de la 
        lista en un string con el fin de poder hacer la busqueda en los diccionarios
    '''
    branch = str(branch)

    # primera linea
    dataFiltered = findElementByKey(data, 'id_branch', branch)
    print(f"{dataFiltered['id_branch']}",
          f"{dataFiltered['city_name']}",
          f"{dataFiltered['department_name']}")

    '''
        patients
    '''

    # segunda linea
    print('patients')

    # tercera linea
    dataFiltered = findElementsByKey(data, 'id_branch', branch)
    print(f"male {len(findElementsByKey(dataFiltered, 'gender', 'm'))} ")

    # cuarta linea
    print(f"female {len(findElementsByKey(dataFiltered, 'gender', 'f'))} ")

    # quinta linea
    print(f"total {len(dataFiltered)} ")

    '''
        medicine quantify
    '''

    # sexta linea
    print('medicine quantity')

    # septima linea
    dataFiltered = findElementsByKey(data, 'id_branch', branch)
    dataFiltered = getDictionaryValues(dataFiltered, 'medicine_quantity')
    average = calculateAverage(dataFiltered)
    print("mean {:.2f}".format(
        average))

    # octava linea
    std = calculateStandardDeviation(dataFiltered, average, True)
    print("std {:.2f}".format(
        std))

    # novena linea
    dataFiltered = convertListData(dataFiltered, 1)
    print(f'min {min(dataFiltered)}')

    # decima linea
    print(f'max {max(dataFiltered)}')

    # onceava linea
    print(f'total {sum(dataFiltered)}')

    '''
        scheduled patients
    '''

    # doceava linea
    print('scheduled patients')

    # treceava linea
    dataFiltered = findElementsByKey(data, 'id_branch', branch)
    dataFiltered = findElementsByKey(dataFiltered, 'gender', 'm')
    dataFiltered = medsDeliveryValidation(dataFiltered)
    print(f'male {len(dataFiltered)}')

    # catorceava linea
    dataFiltered = findElementsByKey(data, 'id_branch', branch)
    dataFiltered = findElementsByKey(dataFiltered, 'gender', 'f')
    dataFiltered = medsDeliveryValidation(dataFiltered)
    print(f'female {len(dataFiltered)}')

    # quinceava linea
    dataFiltered = findElementsByKey(data, 'id_branch', branch)
    dataFiltered = medsDeliveryValidation(dataFiltered)
    print(f'total {len(dataFiltered)}')

    '''
        scheduled medicine quantity
    '''

    # dieciseisava linea
    print('scheduled medicine quantity')

    # diecisieteava linea
    dataFiltered = findElementsByKey(data, 'id_branch', branch)
    dataFiltered = medsDeliveryValidation(dataFiltered)
    dataFiltered = getDictionaryValues(dataFiltered, 'medicine_quantity')
    average = calculateAverage(dataFiltered)
    print("mean {:.2f}".format(
        average))

    # dieciochoava linea
    std = calculateStandardDeviation(dataFiltered, average, True)
    print("std {:.2f}".format(
        std))

    # diecinueveava linea
    dataFiltered = findElementsByKey(data, 'id_branch', branch)
    dataFiltered = medsDeliveryValidation(dataFiltered)
    minElement = minimun(dataFiltered, 'medicine_quantity')

    print(f'min {minElement["medicine_quantity"]}',
          f'{minElement["first_name"]}',
          f'{minElement["last_name"]}',
          f'{minElement["gender"]}',
          f'{minElement["medicine_type"]}',
          )

    # veinteava linea

    maxElement = maximun(dataFiltered, 'medicine_quantity')

    print(f'max {maxElement["medicine_quantity"]}',
          f'{maxElement["first_name"]}',
          f'{maxElement["last_name"]}',
          f'{maxElement["gender"]}',
          f'{maxElement["medicine_type"]}',
          )

    # veintiunava linea
    dataFiltered = findElementsByKey(data, 'id_branch', branch)
    dataFiltered = medsDeliveryValidation(dataFiltered)
    dataFiltered = getDictionaryValues(dataFiltered, 'medicine_quantity')
    dataFiltered = convertListData(dataFiltered, 1)
    print(f'total {sum(dataFiltered)}')
