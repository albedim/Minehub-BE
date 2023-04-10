from flask import jsonify
from minehub.model.entity.News import News
from minehub.model.repository.NewsRepository import NewsRepository
from minehub.service.users.UserPermissionsService import UserPermissionsService
from minehub.service.users.UserService import UserService
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
        newses: list[News] = NewsRepository.getNewses()
        result: list[dict] = []
        for news in newses:
            owner: dict = UserService.getUser(news.owner_id)
            result.append(news.toJson_Owner(owner))
        return jsonify(result)

    @classmethod
    def exists(cls, newsId):
        return NewsRepository.getNews(newsId) is not None

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

    @classmethod
    def remove(cls, userId, newsId):
        if cls.exists(newsId):
            if UserPermissionsService.isStaffer(userId):
                NewsRepository.remove(newsId)
                return Utils.createSuccessResponse(True, Constants.CREATED)
            else:
                return Utils.createWrongResponse(False, Constants.NOT_ENOUGH_PERMISSIONS, 403), 403
        else:
            return Utils.createWrongResponse(False, Constants.NOT_FOUND, 404), 404