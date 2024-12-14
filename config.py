from peewee import SqliteDatabase, Model, IntegerField, CharField, TextField
from flask_login import UserMixin

db = SqliteDatabase("db.sqlite")


class User(UserMixin, Model):
    id = IntegerField(primary_key=True)
    name = CharField(unique=True)
    email = CharField(unique=True)
    password = TextField()

    class Meta:
        database = db
        table_name = "users"


db.create_tables([User])
