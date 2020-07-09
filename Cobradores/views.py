from Cobradores.models import Cobrador

def Crear(cedula,nombre,telefono):
    cobrador=Cobrador(cedula=cedula,nombre=nombre,telefono=telefono)
    cobrador.save()
    print("Se ha creado Un cobrador ",cobrador.id)
    return cobrador.id

def Actualizar(id,cedula,nombre,telefono):
    cobrador=Cobrador.get(id=id)
    cobrador.cedula = cedula
    cobrador.nombre=nombre
    cobrador.telefono=telefono
    cobrador.save()
    return cobrador.id

def CambiarEstado(id):
    cobrador=Cobrador.get(id=id)
    cobrador.estado=False
    cobrador.save()
    return cobrador.id

def Eliminar(id):
    Cobrador.delete().where(Cobrador.id == id).execute()
    return 0


def ListarCobrador():
    return Cobrador.select().where(Cobrador.estado ==True)

def Buscar_NombreCobrador(nombre):
    result=Cobrador.select().where(Cobrador.nombre.contains(nombre) & (Cobrador.estado==True))
    for ciudad in result:
        print(ciudad.id,ciudad.nombre)
    return result

def getCobrador(id):
    return Cobrador.get(id=id)