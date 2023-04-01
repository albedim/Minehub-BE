import datetime

from minehub.configuration.config import sql
from minehub.utils.Constants import Constants


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 05/03/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the category entity
#


class Question(sql.Model):
    __tablename__ = 'questions'
    question_id: int = sql.Column(sql.Integer, primary_key=True)
    category_id: int = sql.Column(sql.Integer, nullable=False)
    name: str = sql.Column(sql.String(64), nullable=False)
    owner_id: int = sql.Column(sql.Integer, nullable=False)
    status: str = sql.Column(sql.String(40), nullable=False)
    closed: bool = sql.Column(sql.Boolean, nullable=False)
    created_on: datetime = sql.Column(sql.String(40), nullable=False)

    def __init__(self, name, owner_id, category_id):
        self.name = name
        self.closed = False
        self.created_on = datetime.datetime.now()
        self.status = Constants.QUESTION_STATUS['JUST_CREATED']
        self.owner_id = owner_id
        self.category_id = category_id

    def toJson(self):
        return {
            'category_id': self.category_id,
            'question_id': self.question_id,
            'status': self.status,
            'created_on': str(self.created_on),
            'owner_id': self.owner_id,
            'name': self.name,
            'closed': self.closed
        }

    def toJson_Owner(self, owner):
        return {
            'category_id': self.category_id,
            'question_id': self.question_id,
            'status': self.status,
            'created_on': str(self.created_on),
            'owner_id': self.owner_id,
            'name': self.name,
            'closed': self.closed,
            'owner': owner
        }

    def toJson_Owner_Messages(self, owner, messages):
        return {
            'category_id': self.category_id,
            'question_id': self.question_id,
            'status': self.status,
            'created_on': str(self.created_on),
            'owner_id': self.owner_id,
            'name': self.name,
            'closed': self.closed,
            'owner': owner,
            'messages': messages
        }