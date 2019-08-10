import json

from flask import Blueprint, request, Response

from svc.controllers.vending_machine_controller import controller

route_blueprint = Blueprint('route_blueprint', __name__)


@route_blueprint.route('/healthCheck', methods=['GET'])
def health_status():
    return 'Success'


@route_blueprint.route('/purchase', methods=['POST'])
def purchase():
    body = json.loads(request.data)

    response, succeeded = controller(body['selection'], body['coins'])
    json_response = json.dumps(response)

    if succeeded:
        return Response(json_response, status=200)
    else:
        return Response(json_response, status=400)
