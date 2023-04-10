from sqlalchemy import desc
from minehub.configuration.config import sql
from minehub.model.entity.News import News


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 09/03/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the news service
#

class NewsRepository():

    @classmethod
    def getNewses(cls):
        news: list[News] = sql.session.query(News).order_by(desc(News.created_on)).all()
        return news

    @classmethod
    def getNews(cls, newsId):
        news: News = sql.session.query(News).filter(News.news_id == newsId).first()
        return news

    @classmethod
    def add(cls, title, body, ownerId):
        news: News = News(title, ownerId, body)
        sql.session.add(news)
        sql.session.commit()

    @classmethod
    def remove(cls, newsId):
        news: News = sql.session.query(News).filter(News.news_id == newsId).delete()
        sql.session.commit()
