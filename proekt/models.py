from peewee import *

db = SqliteDatabase("proekt.db")

class User(Model):
    class Meta:
        database = db
        db_table = "Users"
    vk_id = IntegerField()
    user = TextField()
    other = TextField()
    monsters = TextField()
    lvls = TextField()

class Boss(Model):
    class Meta:
        database = db
        db_table = "Boss"
    stats = TextField()


if __name__ == '__main__':
    db.create_tables([User])
    db.create_tables([Boss])