from minehub.configuration.config import sql


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 31/03/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the role entity
#


class Role(sql.Model):
    __tablename__ = 'roles'
    role_id: int = sql.Column(sql.Integer, primary_key=True)
    color: str = sql.Column(sql.String(14), nullable=False)
    role_label: str = sql.Column(sql.String(20), nullable=False)

    def __init__(self, roleLabel, color):
        self.role_label = roleLabel
        self.color = color

    def toJson(self):
        return {
            'role_id': self.role_id,
            'color': self.color,
            'role_label': self.role_label
        }
