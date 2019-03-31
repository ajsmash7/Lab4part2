import peewee

db = peewee.SqliteDatabase('jugglers.sqlite')


class Juggler(peewee.Model):

    """ Represents a Juggler Record in the Database """

    name = peewee.CharField(unique=True)
    country = peewee.CharField()
    catches = peewee.IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f'ID: {self.id}, Name: {self.name}, Country: {self.country}, Catches: {self.catches}'


db.connect()
db.create_tables([Juggler])
