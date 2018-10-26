import click
from flask import current_app
from flask.cli import with_appcontext


@click.command()
@with_appcontext
def hello():
    print('Hello Command')
