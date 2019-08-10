from flask import Blueprint

route_blueprint = Blueprint('route_blueprint', __name__)


@route_blueprint.route('/healthCheck', methods=['GET'])
def health_status():
    return 'Success'
