from peewee import *
from Manejador.DataBase import db

from Cobradores.models import Cobrador
from Ciudades.models import Ciudad

class Cliente(Model):
    interno=CharField(max_length=20,null=True)
    cedula=CharField(max_length=10,unique=True)
    nombres=CharField(max_length=120)
    direccion=CharField(max_length=120)
    telefono=CharField(max_length=10)
    ciudad=ForeignKeyField(Ciudad)
    zona=CharField(max_length=30)
    cobrador=ForeignKeyField(Cobrador)
    estado=BooleanField(default=True)

    class Meta:
        database = db
# migrate(
#     migrator.rename_column("Cliente",'interno',Cliente.interno)
# )
# migrate(
#     migrator.rename_column('Cliente', 'CEDULA', 'cedula'),
#     migrator.rename_column('Cliente', 'NOMBRES', 'nombres'),
#     migrator.rename_column('Cliente', 'TELEFONO', 'telefono'),
#     migrator.rename_column('Cliente', 'DIRECCION', 'direccion'),
#     migrator.rename_column('Cliente', 'CIUDAD_id', 'ciudad_id'),
#     migrator.rename_column('Cliente', 'ZONA', 'zona'),
#     migrator.rename_column('Cliente', 'COBRADOR_id', 'cobrador_id'),
#     migrator.rename_column('Cliente', 'ESTADO', 'estado'),
# )
db.create_tables([Cobrador])
db.create_tables([Ciudad])
db.create_tables([Cliente])