import json

mis_datos = {
    "Nombre": "Juan",
    "Apellido" : "Perez",
    "Edad" : 30,
    "Ciudad": "Bogota"
}

datosjson = "datos.json"

with open(datosjson, "w") as archivo:
    
    json.dump(mis_datos, archivo)
    
print(f"Los datos se han escrito en '{datosjson}'")