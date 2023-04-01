from minehub.configuration.config import sql
from minehub.model.entity.Role import Role


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 31/03/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the role repository
#

class RoleRepository():

    @classmethod
    def getRoles(cls):
        roles: list[Role] = sql.session.query(Role).all()
        return roles

    @classmethod
    def getRole(cls, roleId):
        role: Role = sql.session.query(Role).filter(Role.role_id == roleId).first()
        return role

    @classmethod
    def add(cls, roleLabel, color):
        role: Role = Role(roleLabel, color)
        sql.session.add(role)
        sql.session.commit()

    @classmethod
    def remove(cls, roleId):
        role: Role = sql.session.query(Role).filter(Role.role_id == roleId).delete()
        sql.session.commit()

    @classmethod
    def exists(cls, roleLabel):
        role: Role = sql.session.query(Role).filter(Role.role_label == roleLabel).first()
        return role
