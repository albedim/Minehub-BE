from minehub.model.entity.Role import Role
from minehub.model.repository.RoleRepository import RoleRepository
from minehub.utils.Constants import Constants
from minehub.utils.Utils import Utils


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 31/03/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the role servce
#

class RoleService():

    @classmethod
    def getRoles(cls):
        roles: list[Role] = RoleRepository.getRoles()
        return Utils.createList(roles)

    @classmethod
    def getRole(cls, roleId):
        role: Role = RoleRepository.getRole(roleId)
        return role.toJson()

    @classmethod
    def add(cls, request):
        try:
            if cls.exists(request['role_label']):
                return Utils.createWrongResponse(False, Constants.ALREADY_CREATED, 409), 409
            else:
                RoleRepository.add(request['role_label'], request['color'])
                return Utils.createSuccessResponse(True, Constants.CREATED)
        except KeyError:
            return Utils.createWrongResponse(False, 400, Constants.INVALID_REQUEST), 400

    @classmethod
    def exists(cls, roleLabel):
        role: Role = RoleRepository.exists(roleLabel)
        return role is not None

    @classmethod
    def remove(cls, roleId):
        RoleRepository.remove(roleId)
        return Utils.createSuccessResponse(True, Constants.CREATED)
