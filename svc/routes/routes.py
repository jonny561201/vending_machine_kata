import json

from flask import Blueprint

from svc.controllers.vending_machine_controller import controller

route_blueprint = Blueprint('route_blueprint', __name__)


@route_blueprint.route('/healthCheck', methods=['GET'])
def health_status():
    return 'Success'


@route_blueprint.route('/purchase', methods=['POST'])
def purchase():
    response = controller(None, None)
    return json.dumps(response)
