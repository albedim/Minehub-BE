from datetime import datetime

from minehub.configuration.config import sql

#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 09/03/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the news entity
#


class News(sql.Model):
    __tablename__ = 'newses'
    news_id: int = sql.Column(sql.Integer, primary_key=True)
    owner_id: int = sql.Column(sql.Integer, nullable=False)
    title: str = sql.Column(sql.String(240), nullable=False)
    body: str = sql.Column(sql.String(1450), nullable=False)
    created_on: datetime = sql.Column(sql.String(40), nullable=False)

    def __init__(self, title, ownerId, body):
        self.title = title
        self.owner_id = ownerId
        self.body = body
        self.created_on = datetime.now()

    def toJson(self):
        return {
            'news_id': self.news_id,
            'title': self.title,
            'body': self.body,
            'owner_id': self.owner_id,
            'created_on': self.created_on
        }

    def toJson_Owner(self, user):
        return {
            'news_id': self.news_id,
            'title': self.title,
            'body': self.body,
            'owner_id': self.owner_id,
            'created_on': self.created_on,
            'owner': user
        }