from Clientes.models import Cliente
from Productos.models import Tarjeta


def Crear(cedula,nombre,telefono,direccion,ciudad,zona,cobrador,interno):
    cliente=Cliente(cedula=cedula,nombres=nombre,
                    telefono=telefono,direccion=direccion,
                    ciudad=ciudad,zona=zona,cobrador=cobrador,interno=interno)
    cliente.save()
    print("Se ha creado Un Cliente ",cliente.id)
    return cliente.id

def Actualizar(id,cedula,nombres,telefono,direccion,ciudad,zona,cobrador,interno):
    cliente=Cliente.get(id=id)
    cliente.cedula = cedula
    cliente.nombres=nombres
    cliente.telefono=telefono
    cliente.direccion=direccion
    cliente.ciudad=ciudad
    cliente.zona=zona
    cliente.cobrador=cobrador
    cliente.interno=interno
    cliente.save()
    return cliente.id

def CambiarEstado(id):
    cliente=Cliente.get(id=id)
    cliente.estado=False
    cliente.save()
    return cliente.id

def Eliminar(id):
    Cliente.delete().where(Cliente.id == id).execute()
    return 0


def ListarClientes():
    return Cliente.select().where(Cliente.estado ==True)

def Buscar_Nombre(nombre):
    result=Cliente.select().where(Cliente.nombres.contains(nombre) & (Cliente.estado==True))
    for cliente in result:
        print(cliente.id,cliente.nombres,cliente.ciudad.nombre)
    return result

def getCliente(id):
    return Cliente.get(id=id)

#*************************** tarjetas del cliente*************************#
def ListarTarjetas(id):
    return Tarjeta.select().where(Tarjeta.venta_id ==id)

def RegistrarPago(venta,fecha,abono,cobrador,recibo):
    result=Tarjeta(venta=venta,fecha=fecha,abono=abono,cobrador=cobrador,recibo=recibo)
    result.save()
    print("Se creo una tarjeta con id: ",result)
    return result.id