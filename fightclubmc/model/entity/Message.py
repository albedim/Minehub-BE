from datetime import datetime

from fightclubmc.configuration.config import sql


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 06/03/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the message entity
#

class Message(sql.Model):
    __tablename__ = 'messages'
    message_id: int = sql.Column(sql.Integer, primary_key=True)
    likes: int = sql.Column(sql.Integer, nullable=False)
    question_id: int = sql.Column(sql.Integer, nullable=False)
    owner_id: int = sql.Column(sql.Integer, nullable=False)
    created_at: datetime = sql.Column(sql.Date, nullable=False)
    body: str = sql.Column(sql.String(450), nullable=False)

    def __init__(self, questionId, ownerId, body):
        self.question_id = questionId
        self.owner_id = ownerId
        self.likes = 0
        self.created_at = datetime.now()
        self.body = body

    def toJson(self):
        return {
            'message_id': self.message_id,
            'likes': self.likes,
            'question_id': self.question_id,
            'owner_id': self.question_id,
            'created_at': self.created_at,
            'body': self.body
        }

    def toJson_Owner(self, owner, likeable, editable, removable):
        return {
            'message_id': self.message_id,
            'likes': self.likes,
            'question_id': self.question_id,
            'owner_id': self.owner_id,
            'created_at': self.created_at,
            'body': self.body,
            'owner': owner,
            'likeable': likeable,
            'editable': editable,
            'removable': removable
        }