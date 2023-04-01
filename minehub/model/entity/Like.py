from minehub.configuration.config import sql

#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 06/03/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the like entity
#


class Like(sql.Model):
    __tablename__ = 'likes'
    like_id: int = sql.Column(sql.Integer, primary_key=True)
    message_id: int = sql.Column(sql.Integer, nullable=False)
    user_id: int = sql.Column(sql.Integer, nullable=False)

    def __init__(self, message_id, user_id):
        self.message_id = message_id
        self.user_id = user_id

    def toJson(self):
        return {
            'like_id': self.like_id,
            'message_id': self.message_id,
            'user_id': self.user_id
        }