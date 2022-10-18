ayunas = str(input())
glucosa = float(input())

if ayunas == 'si':
    if glucosa < 0.44:
        print("hipoglusemia")
    elif glucosa >= 0.44 and glucosa < 0.61:
        print("normal")
    elif glucosa >= 0.61 and glucosa < 0.7:
        print("elevado")
    elif glucosa >= 0.7:
        print("diabetes")
elif ayunas == 'no':
    if glucosa < 0.78:
        print("normal")
    elif glucosa >= 0.78 and glucosa < 1.1:
        print("elevado")
    elif glucosa >= 1.1:
        print("diabetes")
else:
    print("error en los datos")
