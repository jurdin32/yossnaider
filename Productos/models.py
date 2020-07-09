from peewee import *
from playhouse.migrate import migrate, MySQLMigrator

from Manejador.DataBase import db

migrator =MySQLMigrator(db)

from Clientes.models import Cliente
from Cobradores.models import Cobrador

class Producto(Model):
    nombre=CharField(max_length=120)
    detalle=TextField()
    precio_compra=DecimalField(max_digits=9,decimal_places=2)
    marca=CharField(max_length=60)
    serie=CharField(max_length=60)
    estado=BooleanField(default=True)

    class Meta:
        database = db

class Venta(Model):
    cliente=ForeignKeyField(Cliente)
    fecha=DateField()
    valor=DecimalField(max_digits=9,decimal_places=2)
    estado=BooleanField(default=True)

    class Meta:
        database = db

class DetalleVenta(Model):
    venta=ForeignKeyField(Venta)
    fecha=DateField()
    producto=ForeignKeyField(Producto)
    cantidad=IntegerField(default=1)
    valor=DecimalField(max_digits=9,decimal_places=2)
    ganancia = DecimalField(max_digits=9, decimal_places=2,default="0.00")
    total=DecimalField(max_digits=9,decimal_places=2)

    class Meta:
        database = db

# migrate(
#     migrator.add_column("DetalleVenta","ganancia",DetalleVenta.ganancia),
#
# )


class Tarjeta(Model):
    venta=ForeignKeyField(Venta)
    fecha=DateField()
    abono=DecimalField(max_digits=9,decimal_places=2)
    cobrador=ForeignKeyField(Cobrador)
    recibo=CharField(max_length=30,null=True,default="0000000000")

    class Meta:
        database = db


# migrate(
#     migrator.add_column("Tarjeta","recibo",Tarjeta.recibo),
#
# )

class Kardex(Model):
    producto=ForeignKeyField(Producto,null=True)
    detalle=TextField()
    tipo=CharField(max_length=2)
    fecha=DateField()
    cantidad =IntegerField()
    precio_compra = DecimalField(max_digits=9, decimal_places=2)
    precio_venta = DecimalField(max_digits=9, decimal_places=2)
    total_compra=DecimalField(max_digits=9, decimal_places=2)
    total_venta=DecimalField(max_digits=9, decimal_places=2)
    venta=ForeignKeyField(Venta,null=True, default=1)

    class Meta:
        database = db

# migrate(
    # migrator.add_column("Kardex","venta_id",Kardex.venta)
    # migrator.rename_column("Kardex",'producto',"producto_id"),
# migrator.rename_column("Kardex",'DETALLE','detalle'),
# migrator.rename_column("Kardex",'TIPO','tipo'),
# migrator.rename_column("Kardex",'FECHA','fecha'),
# migrator.rename_column("Kardex",'CANTIDAD','cantidad'),
# migrator.rename_column("Kardex",'PRECIO_COMPRA','precio_compra'),
# migrator.rename_column("Kardex",'PRECIO_VENTA','precio_venta'),
# migrator.rename_column("Kardex",'TOTAL_COMPRA','total_compra'),
# migrator.rename_column("Kardex",'TOTAL_VENTA','total_venta'),
# )

db.create_tables([Producto,Venta,DetalleVenta,Tarjeta,Kardex])

