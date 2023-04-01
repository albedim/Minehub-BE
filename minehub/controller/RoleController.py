from flask import Blueprint, request
from flask_cors import cross_origin
from minehub.service.RoleService import RoleService
from minehub.utils.Utils import Utils


role: Blueprint = Blueprint('RoleController', __name__, url_prefix=Utils.getURL('role'))


@role.route("/get", methods=['GET'])
@cross_origin()
def get():
    return RoleService.getRoles()


@role.route("/add", methods=['POST'])
@cross_origin()
def add():
    return RoleService.add(request.json)


@role.route("/remove/<roleId>", methods=['DELETE'])
@cross_origin()
def remove(roleId):
    return RoleService.remove(roleId)