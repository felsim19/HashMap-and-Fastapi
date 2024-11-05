with open ('nombres.csv', 'r')as txt:
    contenido = txt.readlines()
    nombrelista = []
    nombres_femeninos = []
    nombres_masculinos = []
    
    for i in contenido[1:900000]:
        x = i.split(",")
        nombres = x[3]
        sexo = x[1]
        nombrelista.append(nombres)
        if sexo == "F":
            nombres_femeninos.append(nombres)
        elif sexo == "M":
            nombres_masculinos.append(nombres)
        print("NOMBRES:")
        print(nombrelista)
        print(f"En la lista de nombres hay {len(nombrelista)} nombres")
        print("NOMBRES FEMENINOS:")
        print(nombres_femeninos)
        print(f"En la lista de nombres femeninos hay {len(nombres_femeninos)} nombres")
        print("NOMBRES MASCULINOS:")
        print(nombres_masculinos)
        print(f"En la lista de nombres masculinos hay {len(nombres_masculinos)} nombres")
        
    