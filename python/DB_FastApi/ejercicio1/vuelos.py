import firebase_admin
from firebase_admin import credentials, firestore
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


cre = credentials.Certificate('C:/Users/57310/OneDrive/Documentos/senaa/ADSO/4 Trimestre/python/DB_FastApi/ejercicio1/reservavuelos-485fe-firebase-adminsdk-ppf3e-b63b480a05.json')

firebase_admin.initialize_app(cre)

db = firestore.client()

@app.get("/InformacionLatam/{Id}")
async def consulta(Id:str):
    datos = db.collection('Latam').document(Id).get()
    if datos.exists:
        return {datos.id:datos.to_dict()}
    else:
        raise HTTPException(status_code=404,detail="El documento no existe")
        

@app.get("/InformacionAvianca/{Id}")
async def consulta(Id:str):
    datos = db.collection('Avianca').document(Id).get()
    if datos.exists:
        return {datos.id:datos.to_dict()}
    else:
        raise HTTPException(status_code=404,detail="El documento no existe")

@app.get("/HorariosVuelos")
async def consulta():
    datosLatam = db.collection('Latam').get()
    datosAvianca = db.collection('Avianca').get()
    Horarios = []
    for doc in datosLatam:
        data = doc.to_dict()
        if 'inicio vuelo' in data and 'fin vuelo' in data:
            Horarios.append({
                'aerolina' : 'Latam',
                'inicio vuelo' : data.get('inicio vuelo'),
                'fin vuelo' : data.get('fin vuelo')
            })
    
    for doc in datosAvianca:
        data = doc.to_dict()
        if 'inicio vuelo' in data and 'fin vuelo' in data:
            Horarios.append({
                'aerolinea' : 'Avianca',
                'inicio vuelo' : data.get('inicio vuelo'),
                'fin vuelo' : data.get('fin vuelo')
            })
    return Horarios

@app.get("/TarifasVuelo")
async def consulta():
    datosLatam = db.collection('Latam').get()
    datosavianca = db.collection('Avianca').get()
    tarifas = []
    for doc in datosLatam:
        data = doc.to_dict()
        if 'origen' in data and 'destino' in data and 'tarifa' in data:
            tarifas.append({
                'aerolinea' : 'Latam',
                'Origen' : data.get('origen'),
                'Destino' : data.get('destino'),
                'Tarifa' : data.get('tarifa')
            })
    
    for doc in datosavianca:
        data = doc.to_dict()
        if 'origen' in data and 'destino' in data and 'tarifa' in data:
            tarifas.append({
                'aerolinea' : 'Avianca',
                'Origen' : data.get('origen'),
                'Destino' : data.get('destino'),
                'Tarifa' : data.get('tarifa')
            })
    return tarifas