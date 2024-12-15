import datetime
from peewee import SqliteDatabase, Model, IntegerField, CharField, TextField, TimestampField, ForeignKeyField
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


class Message(Model):
    id = IntegerField(primary_key=True)
    user = ForeignKeyField(User, backref="messages", on_delete="CASCADE")  # 参照先が削除された場合は削除する
    content = TextField()
    pub_date = TimestampField(default=datetime.datetime.now)
    reply_to = ForeignKeyField(
        "self", backref="messages", on_delete="CASCADE", null=True
    )  # 参照先が削除された場合は削除する nullを許容する

    class Meta:
        database = db
        table_name = "messages"


db.create_tables([User, Message])
db.pragma("foreign_keys", 1, permanent=True)  # on_deleteを動作させるオプション設定を追加
