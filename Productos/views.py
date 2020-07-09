from Productos.models import Producto, Kardex


def Crear(nombre,detalle,precio_compra,marca,serie):
    producto=Producto(nombre=nombre,detalle=detalle,precio_compra=precio_compra,marca=marca,serie=serie)
    producto.save()
    print("Se ha creado Un Producto ",producto.id)
    return producto.id

def Actualizar(id,nombre,detalle,precio_compra,marca,serie):
    producto=Producto.get(id=id)
    producto.nombre=nombre
    producto.detalle=detalle
    producto.precio_compra=precio_compra
    producto.marca=marca
    producto.serie=serie
    producto.save()
    return producto.id

def CambiarEstado(id):
    producto=Producto.get(id=id)
    producto.estado=False
    producto.save()
    return producto.id

def Eliminar(id):
    Producto.delete().where(Producto.id == id).execute()
    return 0


def ListarProductos():
    return Producto.select().where(Producto.estado ==True)

def Buscar_NombreProducto(nombre):
    result=Producto.select().where((Producto.nombre.contains(nombre)|Producto.detalle.contains(nombre))  & (Producto.estado==True))
    return result

def getProducto(id):
    return Producto.get(id=id)


#********************************** kardex **********************************

def CrearRegstroKardex(prod_id,detalle,tipo,fecha,cantidad,precio_compra,precio_venta,total_compra,total_venta,venta):
    kardex=Kardex(
        producto=prod_id,
        detalle = detalle,
        tipo = tipo,
        fecha = fecha,
        cantidad = cantidad,
        precio_compra = precio_compra,
        precio_venta = precio_venta,
        total_compra = total_compra,
        total_venta = total_venta,
        venta=venta
    ).save()

def ListarKardex():
    return Kardex

def ListarKardexProducto(producto_id):
    return Kardex.select().where(Kardex.producto_id==producto_id)

def EliminarRegistroKardex(venta_id):
    Kardex.delete().where(Kardex.venta_id == venta_id).execute()
    return 0

def Contador(id_producto):
    registros= Kardex.select().where(Kardex.producto_id == id_producto)
    ingresos=0
    egresos=0
    for reg in registros:
        if reg.tipo=="I":
            ingresos+=reg.cantidad
        else:
            egresos+=(reg.cantidad)
    print("total ingreso",ingresos,"total egresos", egresos,"=",ingresos-egresos)
    return ingresos-egresos