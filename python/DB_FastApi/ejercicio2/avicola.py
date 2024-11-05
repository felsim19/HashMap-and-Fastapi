import firebase_admin
from firebase_admin import credentials, firestore
from fastapi import FastAPI, HTTPException

app = FastAPI()

cre = credentials.Certificate('C:/Users/57310/OneDrive/Documentos/senaa/ADSO/4 Trimestre/python/DB_FastApi/ejercicio2/avicola-6aa9e-firebase-adminsdk-8zab8-d12a912916.json')

firebase_admin.initialize_app(cre)

db = firestore.client

