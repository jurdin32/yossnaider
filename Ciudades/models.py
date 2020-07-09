from peewee import *
from Manejador.DataBase import db


class Ciudad(Model):
    nombre=CharField(max_length=60)
    estado=BooleanField(default=True)

    class Meta:
        database = db
