from flask import jsonify

from minehub.model.entity.Message import Message
from minehub.model.repository.MessageRepository import MessageRepository
from minehub.model.repository.LikeRepository import LikeRepository
from minehub.service.LikeService import LikeService
from minehub.service.UserService import UserService
from minehub.utils.Constants import Constants
from minehub.utils.Utils import Utils


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 05/03/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the server service
#

class MessageService():

    @classmethod
    def getAllMessages(cls):
        messages: list[Message] = MessageRepository.getAllMessages()
        return Utils.createList(messages)

    @classmethod
    def getMessages(cls, userId, questionId):
        messages: list[Message] = MessageRepository.getMessages(questionId)
        result: list[dict] = []
        for message in messages:
            owner: dict = UserService.getUser(message.owner_id)
            result.append(message.toJson_Owner(
                owner,
                likeable=LikeService.get(userId, message.message_id) is None,
                editable=userId == message.owner_id,
                removable=userId == message.owner_id or UserService.getUser(userId)['admin'])
            )
        return jsonify(result)

    @classmethod
    def getMessagesByCategory(cls, categoryId):
        messages: list[Message] = MessageRepository.getMessagesByCategory(categoryId)
        return Utils.createList(messages)

    @classmethod
    def add(cls, request):
        try:
            user: dict = UserService.getUser(request['owner_id'])
            if user['banned']:
                return Utils.createWrongResponse(False, 306, Constants.NOT_ENOUGH_PERMISSIONS), 306
            else:
                MessageRepository.add(request['question_id'], request['owner_id'], request['body'])
                UserService.addMessage(request['owner_id'])
            return Utils.createSuccessResponse(True, Constants.CREATED)
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 400), 400

    @classmethod
    def changeMessage(cls, request):
        MessageRepository.changeMessage(request['message_id'], request['body'])
        return Utils.createSuccessResponse(True, Constants.CREATED)
        
    @classmethod
    def removeMessage(cls, owner, messageId):
        message: Message = MessageRepository.get(messageId)
        if owner['admin'] or message.owner_id == owner['user_id']:
            MessageRepository.removeMessage(messageId)
            LikeRepository.removeLikes(messageId)
            UserService.removeMessage(owner['user_id'])
            return Utils.createSuccessResponse(False, Constants.CREATED), 200
        else:
            return Utils.createWrongResponse(False, Constants.NOT_ENOUGH_PERMISSIONS, 403), 403
