from model import Juggler
from peewee import *

db_file = "jugglers.sqlite"

# refactor database to peewee


def add_record(juggler):
    """ adds a new juggler to the database. Will error if Juggler already exists
        :param juggler to be added
        :raises JugglerError if duplicate"""
    try:
        juggler.save()
    except IntegrityError as e:
        raise JugglerError('Juggler Record Already Exists') from e


def delete_juggler(name):
    """ deletes a juggler from the database. Will error if Juggler does not exist
            :param name of the juggler to be deleted
            :raises JugglerError if not found"""
    record_deleted = Juggler.delete().where(Juggler.name == name).execute()
    if not record_deleted:
        raise JugglerError('Juggler Record Not Found')


def search_records(entry):
    """ searches for a juggler in the database.
                :param entry search term from user
                :returns a list of the query results"""
    query = Juggler.select().where(Juggler.name.contains(entry))
    return list(query)


def get_jugglers():
    """ returns a list of all the juggler records in the database.
                    :returns a list of the query results for all records"""
    query = Juggler.select()
    return list(query)


def update_catches(name, catches):
    """ updates a juggler's catches in the database by name, though in real world id would be preferred.
            Will error if Juggler does not exist
                :param name : the name of the juggler to be updated
                 :param catches : the new number of catches
                :raises JugglerError if juggler not found"""

    row_modified = Juggler.update(catches=catches).where(Juggler.name == name).execute()
    if not row_modified:
        raise JugglerError(f'Juggler {name} was not found.')


class JugglerError(Exception):
    # for raise errors
    pass
