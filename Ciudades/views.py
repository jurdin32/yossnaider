from Ciudades.models import Ciudad

def Crear(nombre):
    ciudad=Ciudad(nombre=nombre)
    ciudad.save()
    print("Se ha creado Una ciudad ",ciudad.id)
    return ciudad.id

def Actualizar(id,nombre):
    ciudad=Ciudad.get(id=id)
    ciudad.nombre=nombre
    ciudad.save()
    return ciudad.id

def CambiarEstado(id):
    ciudad=Ciudad.get(id=id)
    ciudad.estado=False
    ciudad.save()
    return ciudad.id

def Eliminar(id):
    Ciudad.delete().where(Ciudad.id == id).execute()
    return 0


def Listar():
    return Ciudad.select().where(Ciudad.estado ==True)

def Buscar_Nombre(nombre):
    result=Ciudad.select().where(Ciudad.nombre.contains(nombre) & (Ciudad.estado==True))
    for ciudad in result:
        print(ciudad.id,ciudad.nombre)
    return result

def getCiudad(id):
    return Ciudad.get(id=id)