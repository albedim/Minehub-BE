from flask import Blueprint
from flask_cors import cross_origin
from minehub.service.ServerService import ServerService
from minehub.utils.Utils import Utils


server: Blueprint = Blueprint('ServerController', __name__, url_prefix=Utils.getURL('server'))


@server.route("/get", methods=['GET'])
@cross_origin()
def signin():
    return ServerService.get()


@server.route("/maintenance", methods=['GET'])
@cross_origin()
def maintenance():
    return ServerService.maintenance()


@server.route("/maintenance/<status>", methods=['PUT'])
@cross_origin()
def setMaintenance(status):
    return ServerService.setMaintenance(status)