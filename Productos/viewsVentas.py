from Clientes.models import Cliente
from Productos.models import Venta,DetalleVenta


def Crear(cliente_id,fecha,valor):
    venta=Venta(cliente_id=cliente_id,fecha=fecha,valor=valor)
    venta.save()
    print("Se ha creado Una Nota de Venta ",venta.id)
    return venta.id

def Actualizar(id,cliente_id,fecha,valor):
    venta=Venta.get(id=id)
    venta.cliente=Cliente.get(id=cliente_id)
    venta.fecha=fecha
    venta.valor=valor
    venta.save()
    return venta.id

def CambiarEstado(id):
    venta=Venta.get(id=id)
    venta.estado=False
    venta.save()
    return venta.id

def Eliminar(id):
    Venta.delete().where(Venta.id == id).execute()
    return 0


def ListarVentas(estado):
    return Venta.select().where(Venta.estado ==estado)

def ListarVentasCliente(cliente_id):
    return Venta.select().where(Venta.cliente_id==cliente_id)

def Buscar_Ventas(id=0, estado=None,fecha="",todas=True):
    result=None
    print('id',id,'fecha',fecha,'estado',estado)
    if todas:
        result=Venta.select().where(Venta.valor>0)
    if id > 0:
        result = Venta.select().where(Venta.cliente==id)
    if estado!=None:
        print("viene con estado..!",estado)
        result= result.filter(estado=estado)
    if fecha!="":
        print("viene con fecha",fecha)
        result = result.filter(fecha=fecha)

    return result

def getVenta(id):
    return Venta.get(id=id)

def getCountVentas():
    return Venta.select().count()

#********************************** kardex **********************************

def CrearDetalles(venta_id,fecha,producto_id,cantidad,valor,ganancia,total):
    det=DetalleVenta(venta_id=venta_id,fecha=fecha,producto_id=producto_id,cantidad=cantidad,valor=valor,ganancia=ganancia,total=total)
    det.save()
    return det.id

def VerDetalles(venta_id):
    return DetalleVenta.select().where(DetalleVenta.venta==venta_id)


def EliminarDetalle(venta_id):
    DetalleVenta.delete().where(DetalleVenta.venta_id == venta_id).execute()
    return 0
