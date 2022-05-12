import traceback
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def init_db():
    db = get_db()
    '''
    executing following sql file to initialization of table.
    '''
    print("try to run sql")
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """
    Clear the existing data and create new tables.
    :return:
    """
    print("Going to init db from command")
    init_db()
    click.echo("Initialized the database and related table from .")
    print("Finished of running db")


def init_app(app):
    """
    passing flask application from main process. providing table initialization sql
    :param app: flask application context
    :return:
    """
    print("Going to init db")
    app.teardown_appcontext(close_db)
    print("get close exist resource")
    app.cli.add_command(init_db_command)


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
