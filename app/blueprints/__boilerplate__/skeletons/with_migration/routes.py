from flask import Blueprint, current_app
from .commands import init_blueprint_cli

# do not rename "blueprint" variable if you want to use auto import
blueprint: Blueprint = Blueprint(
    '$blueprint_name',
    __name__,
    template_folder='templates'
)

init_blueprint_cli(blueprint)

