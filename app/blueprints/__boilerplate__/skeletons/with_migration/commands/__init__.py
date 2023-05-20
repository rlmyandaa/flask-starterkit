"""
Implement your cli for this blueprint
Don't forget to import in routes.py:

    from app.blueprints.<blueprint_name>.commands import init_blueprint_cli
    init_blueprint_cli(blueprint)
"""
import click

from flask import Blueprint
from flask.cli import with_appcontext
from ..migrations import MODEL_LIST
from app.ext.sqlalchemy.model import BaseModel
from app.ext.sqlalchemy.database import get_engine

@click.command('migrate')
@with_appcontext
def command_migrate():
    for model in MODEL_LIST:
        model: BaseModel = model
        print("Migrating {}".format(model.__name__))
        model_metadata = getattr(model, 'metadata')
        model_metadata.create_all(bind=get_engine())

def init_blueprint_cli(blueprint: Blueprint) -> None:
    blueprint.cli.add_command(command_migrate)
