import json

with open('GLOBANT.csv', 'r')as txt:
    contenido = txt.readlines()
    
with open('analisis_archivo.csv','w')as txt:
    txt.write("Fecha\tComportamiento de la accion\tPunto medio HIGH-LOW\n")
    fechaMenor = ""
    fechaMayor = ""
    mayor = -1
    menor = 9999
    down = 0
    up = 0
    stable = 0
    for i in contenido[1:]:
        x = i.split(",")
        fecha = x[0]
        comportamiento = ""
        if float(x[4]) - float(x[1]) > 0:
            comportamiento = "SUBE"
            up += 1
        elif float(x[4]) - float(x[1]) < 0:
            comportamiento = "BAJA"
            down += 1
        elif float(x[4]) - float(x[1]) == 0:
            comportamiento = "ESTABLE"
            stable += 1
        
        valorAccion = (float(x[2]) - float(x[3]))/2
        txt.write(f"{fecha}\t{comportamiento}\t{valorAccion}\n")
        
        if float(x[3]) < menor:
            menor = float(x[3])
            fechaMenor = x[0]
        if float(x[2]) > mayor:
            mayor = float(x[2])
            fechaMayor = x[0]
    
    data = {
    "date_lowest_price" : fechaMenor,
    "lowest_price" :  menor,
    "date_highest_price" : fechaMayor,
    "highest_price" : mayor,
    "cantidad_veces_sube" : up,
    "cantidad_veces_baja" : down,
    "cantidad_veces_estable" : stable
    }
    
    with open("detalles.json", "w")as archivo:
        json.dump(data, archivo)
    print(f"Los datos se han escrito en '{data}'")