import firebase_admin
from firebase_admin import credentials, firestore
from fastapi import FastAPI, HTTPException
from modelo.modelo import Cliente
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

cre = credentials.Certificate('C:/Users/57310/OneDrive/Documentos/senaa/ADSO/4 Trimestre/python/DB_FastApi/ejemplo/proyect420-473cc-firebase-adminsdk-x5om3-b00d04d995.json')

firebase_admin.initialize_app(cre)

db = firestore.client()

datos = db.collection('Cliente').get()

for i in datos:
    print(f'{i.id} "{i.to_dict()}')
    
    
@app.get("/datosfire")
async def Consultardatosfire():
    datos = db.collection('Cliente').get()
    data = [i.to_dict() for i in datos]
    return data

@app.post("/insertar")
async def Insertar_datos(cliente: Cliente):
    try:
        doc_ref = db.collection('Cliente').add(cliente.dict())
        return {"message" : "Cliente agregado exitosamente", "id":doc_ref[1].id}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))  
    