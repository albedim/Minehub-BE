from minehub.model.entity.Like import Like
from minehub.model.repository.LikeRepository import LikeRepository
from minehub.model.repository.MessageRepository import MessageRepository
from minehub.utils.Constants import Constants
from minehub.service.users.UserService import UserService
from minehub.utils.Utils import Utils


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 06/03/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the like service
#


class LikeService():

    @classmethod
    def add(cls, request):
        try:
            if cls.get(request['user_id'], request['message_id']) is not None:
                return Utils.createWrongResponse(False, Constants.ALREADY_CREATED, 401), 401
            else:
                LikeRepository.add(request['user_id'], request['message_id'])
                MessageRepository.addLike(request['message_id'])
                UserService.addLike(request['user_id'])
                return Utils.createSuccessResponse(True, Constants.CREATED), 200
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 400), 400

    @classmethod
    def remove(cls, userId, messageId):
        LikeRepository.remove(userId, messageId)
        MessageRepository.removeLike(messageId)
        UserService.removeLike(userId)
        return Utils.createSuccessResponse(True, Constants.CREATED)

    @classmethod
    def get(cls, userId, messageId):
        like: Like = LikeRepository.get(userId, messageId)
        return like
