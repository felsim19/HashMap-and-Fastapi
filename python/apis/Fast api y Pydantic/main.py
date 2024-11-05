from fastapi import FastAPI, HTTPException
from model import Producto
from model_user import Usuario
from model_orden import Orden
import json
import re

'''Rutas Productos'''

app = FastAPI()
with open("datos.json", "r")as txt:
    datosProducto = json.load(txt)
    listaProducto = [Producto(**i)for i in datosProducto]

@app.post("/producto", response_model=Producto)
async def Insertar(product:Producto):
    for p in listaProducto:
        if p.Id == product.Id:
            raise HTTPException(status_code=404, detail="No puede crear el mismo id")
        if float(product.Precio) <= 0:
            raise HTTPException(status_code=404, detail="El precio del producto no pueder ser 0 o menor")
        if product.Cantidad < 0:
            raise HTTPException(status_code=404, detail="El cantidad del producto no pueder ser 0 o menor")
    listaProducto.append(product)    
    with open("datos.json", "w")as send:
        json.dump([c.dict() for c in listaProducto], send, indent=4)
        return product

@app.get("/productos")
async def MostrarProductos():
    if not listaProducto:
        raise HTTPException(status_code=404, detail="La lista esta vacia")
    else:
        return listaProducto

@app.get("/ConsultaProducto/{Id}")
async def CosultarProducto(Id:int):
    for i in listaProducto:
        if i.Id == Id:
            return i
    raise HTTPException(status_code=404, detail="Producto No econtrado")

@app.put("/ActualizarProducto/{Id}", response_model=Producto)
async def ActualizarProducto(Id:int,ProductoNuevo:Producto):
    for i, datos in enumerate(listaProducto):
        if datos.Id == Id:
            listaProducto[i] = ProductoNuevo
            with open ("datos.json", "w")as txt:
                json.dump([j.dict() for j in listaProducto], txt, indent=4)
                return ProductoNuevo
    raise HTTPException(status_code=404, detail="El Id no existe") 

@app.delete("/BorrarProducto/{Id}")
async def BorrarProducto(Id:int):
    for d in listaProducto:
        if d.Id == Id:
            listaProducto.remove(d)
            with open("datos.json","w")as txt:
                json.dump([j.dict() for j in listaProducto], txt, indent=4)
                raise HTTPException(status_code=200, detail="Producto Eliminado")
    raise HTTPException(status_code=404, detail="El producto no existe")

@app.get("/PrecioMayor")
async def ConsultarPrecioMayores():
    ProductosMayores = []
    for d in listaProducto:
        if float(d.Precio) >= 500.000:
            ProductosMayores.append(d)
    with open("mayores.json","w")as txt:
        json.dump([p.dict() for p in ProductosMayores],txt,indent=4)
    return ProductosMayores

"""Ruta Usuario"""

with open("user.json", "r")as txt:
    datosUsuario = json.load(txt)
    listaUsuario = [Usuario(**u)for u in datosUsuario]


@app.post("/usuario", response_model=Usuario)
async def UsuarioNuevo(user:Usuario):
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    for i in listaUsuario:
        if i.Id == user.Id:
            raise HTTPException(status_code=404,detail="Los Usuarios no Pueden Tener dos Ids iguales")
        if i.Email == user.Email:
            raise HTTPException(status_code=404,detail="Los Usuarios no Pueden Tener dos emails iguales")
        if not re.match(patron, user.Email):
            raise HTTPException(status_code=404,detail="Email invalido")
        if user.Edad < 18:
            raise HTTPException(status_code=404,detail="Edad Invalidad")
    listaUsuario.append(user)
    with open("user.json", "w")as wrt:
        json.dump([i.dict() for i in listaUsuario],wrt,indent=4)
        return user
    

@app.get("/MostarUsuarios")
async def MostarUsuarios():
    if not listaUsuario:
        raise HTTPException(status_code=404, detail="lista vacia")
    else:
        return listaUsuario
    
@app.get("/obtenerUsuario/{ID}")
async def ObtenerUsraio(ID:int):
    for i in listaUsuario:
        if i.Id == ID:
            return i
    raise HTTPException(status_code=404, detail="usuario No econtrado")

@app.put("/ActualizarUsuario/{ID}", response_model=Usuario)
async def ActualizarUsuario(ID:int, newUser: Usuario):
    for i,datos in enumerate(listaUsuario):
        if datos.Id == ID:
            listaUsuario[i] = newUser
            with open ("user.json", "w")as txt:
                json.dump([i.dict() for i in listaUsuario],txt, indent=4)
                return newUser
    raise HTTPException(status_code=404, detail="No se Encontro el ID")

@app.delete("/BorrarUsuario/{ID}")
async def BorrarUsuario(ID:int):
    for i in listaUsuario:
        if i.Id == ID:
            listaUsuario.remove(i)
            with open("user.json", "w")as txt:
                json.dump([i.dict() for i in listaUsuario],txt,indent=4)
                raise HTTPException(status_code=404,detail="Usuario Borrado")
    raise HTTPException(status_code=404,detail="Usuario No existe")

"""Ruta Orden"""

with open ("orden.json", "r")as read:
    datosOrden = json.load(read)
    listaOrden = [Orden(**i) for i in datosOrden]
    
@app.post("/Orden")
async def CrearOrden(NewOrden:Orden):
    for i in listaOrden:
        if i.ID == NewOrden.ID:
            raise HTTPException(status_code=404, detail="No puedes crear el mismo id")
    usuario_existe = False
    for u in listaUsuario:
        if u.Id == NewOrden.IDUSERS:
            usuario_existe = True
            break
    if not usuario_existe:
        raise HTTPException(status_code=400, detail="El ID del usuario no existe")
    productosValido = []
    for producto_id in NewOrden.Lista_productos:
        for p in listaProducto:
            if p.Id == producto_id:
                productosValido.append(p)
                break
    if len(productosValido) != len(NewOrden.Lista_productos):
        raise HTTPException(status_code=404, detail="no hay ningun producto con este id")
    NewOrden.total = NewOrden.calcularTotal(datosProducto,NewOrden.Lista_productos)
    listaOrden.append(NewOrden)
    with open("orden.json","w")as write:
        json.dump([i.dict() for i in listaOrden], write, indent=4)
        return{f"El usuario es {listaUsuario[NewOrden.IDUSERS-1].Nombre}"
               :f"El total es {NewOrden.total}"}
    
@app.get("/ObtenerOrdenes")
async def mostrarOrden():
    if not listaOrden:
        raise HTTPException(status_code=404,detail="Lista vacia")
    else:
        return listaOrden
    
@app.put("/AcutualizarOrden/{ID}", response_model=Orden)
async def ActualizarOrden(ID:int, ORDENPut:Orden):
    for i, datos in enumerate(listaOrden):
        if datos.ID == ID:
            listaOrden[i] = ORDENPut
            ORDENPut.total = ORDENPut.calcularTotal(datosProducto, ORDENPut.Lista_productos)
            with open("orden.json","w")as write:
                json.dump([i.dict() for i in listaOrden],write,indent=4)
                return ORDENPut
    raise HTTPException(status_code=404,detail="Ese Id no esta en la lista")

@app.delete("/BorrarOrden/{ID}")
async def BorraOrden(ID:int):
    for i in listaOrden:
        if i.ID == ID:
            listaOrden.remove(i)
            with open("orden.json", "w")as txt:
                json.dump([i.dict() for i in listaOrden],txt,indent=4)
                raise HTTPException(status_code=404,detail="Orden Borrado")
    raise HTTPException(status_code=404,detail="Orden No existe")


@app.get("/OrdenesUsuario/{ID}")
async def FiltarOrden(ID:int):
    filtrar = []
    for i in listaOrden:
        if i.IDUSERS == ID:
            filtrar.append(i)
    if not filtrar:
        raise HTTPException(status_code=404,detail="Ese usuario no tiene ordenes")
    else:
        return filtrar
    

@app.get("/TotalGasto/{ID}")
async def TotalCuenta(ID:int):
    ctotal = 0
    for i in listaOrden:
        if i.IDUSERS == ID:
            ctotal += i.total
    return{f"El usuario {listaUsuario[ID].Nombre} ":f"tiene una cuenta total de {ctotal}" }