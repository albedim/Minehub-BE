from flask import jsonify
from minehub.model.entity.News import News
from minehub.model.repository.NewsRepository import NewsRepository
from minehub.service.UserService import UserService
from minehub.utils.Constants import Constants
from minehub.utils.Utils import Utils


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 09/03/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the news service
#


class NewsService():

    @classmethod
    def getNews(cls):
        newses: list[News] = NewsRepository.getNews()
        result: list[dict] = []
        for news in newses:
            owner: dict = UserService.getUser(news.owner_id)
            result.append(news.toJson_Owner(owner))
        return jsonify(result)

    @classmethod
    def add(cls, request):
        try:
            NewsRepository.add(request['title'], request['body'], request['owner_id'])
            users: list = UserService.getAllUsers()
            for user in users:
                Utils.sendNewsEmail(request['title'], request['body'], user['email'])
            return Utils.createSuccessResponse(True, Constants.CREATED)
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 400), 400