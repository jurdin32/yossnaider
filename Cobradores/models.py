from peewee import *
from Manejador.DataBase import db

class Cobrador(Model):
    cedula=CharField(max_length=10,unique=True)
    nombre=CharField(max_length=120)
    telefono=CharField(max_length=10)
    estado=BooleanField(default=True)

    class Meta:
        database = db

# migrate(
#      migrator.add_column('Cobrador','estado',Cobrador.estado)
# )

# migrate(
#     migrator.rename_column('Cobrador', 'CEDULA', 'cedula'),
#     migrator.rename_column('Cobrador', 'NOMBRE', 'nombre'),
#     migrator.rename_column('Cobrador', 'TELEFONO', 'telefono'),
# )
