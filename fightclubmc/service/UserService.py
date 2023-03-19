from datetime import timedelta

from flask import jsonify
from flask_jwt_extended import create_access_token, jwt_required

from fightclubmc.model.entity.User import User
from fightclubmc.model.repository.UserRepository import UserRepository
from fightclubmc.utils.Constants import Constants
from fightclubmc.utils.Utils import Utils
from resources.rest_service import config


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 05/03/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the user service
#


class UserService():

    @classmethod
    def signin(cls, request: dict):
        try:
            user: User = UserRepository.signin(
                request['email'],
                request['password']
            )
            if user is not None:
                return Utils.createSuccessResponse(True, create_access_token(
                    identity=user.toJson(), expires_delta=timedelta(weeks=4)))
            else:
                return Utils.createWrongResponse(False, Constants.NOT_FOUND, 404), 404
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 400), 400

    @classmethod
    def exists(cls, email, minecraftUsername) -> bool:
        return UserRepository.getUserByEmail(email) is not None \
               or UserRepository.getUserByMinecraftUsername(minecraftUsername) is not None

    @classmethod
    def getUser(cls, userId):
        try:
            return UserRepository.getUserById(userId).toJson()
        except AttributeError:
            return Utils.createWrongResponse(False, Constants.NOT_FOUND, 404), 404

    @classmethod
    def signup(cls, request: dict):
        try:
            if not cls.exists(request['email'], request['minecraft_username']):
                UserRepository.signup(
                    request['name'],
                    request['email'],
                    request['minecraft_username'],
                    request['password']
                )
                return Utils.createSuccessResponse(True, Constants.CREATED)
            else:
                return Utils.createWrongResponse(False, Constants.ALREADY_CREATED, 409), 409
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 400), 400

    @classmethod
    def createForgottenPasswordToken(cls, email):
        user: User = UserRepository.getUserByEmail(email)
        if user is None:
            return Utils.createWrongResponse(False, Constants.NOT_FOUND, 404), 404
        else:
            token: str = Utils.createLink(140)
            UserRepository.createForgottenPasswordToken(user, token)
            Utils.sendPasswordForgottenEmail(user.email, token)
            return Utils.createSuccessResponse(True, Constants.CREATED), 200

    @classmethod
    def getUserByPasswordForgottenToken(cls, token):
        user: User = UserRepository.getUserByPasswordForgottenToken(token)
        if user is None:
            return Utils.createWrongResponse(False, Constants.NOT_FOUND, 404), 404
        else:
            return Utils.createSuccessResponse(True, user.user_id), 200

    @classmethod
    def changePassword(cls, request):
        try:
            UserRepository.changePassword(request['user_id'], Utils.hash(request['new_password']))
            return Utils.createSuccessResponse(True, Constants.CREATED)
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 400), 400

    @classmethod
    def getStaffers(cls):
        return Utils.createList(UserRepository.getStaffers())

    @classmethod
    def getAllUsers(cls):
        return Utils.createList(UserRepository.getAllUsers())

    @classmethod
    def getRecent(cls):
        return Utils.createList(UserRepository.getRecent())

    @classmethod
    def admin(cls, request):
        try:
            if request['username'] == config['admin']['username'] and request['password'] == config['admin']['password']:
                return Utils.createSuccessResponse(True, True)
            else:
                return Utils.createWrongResponse(False, False, 404), 404
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 400), 400

    @classmethod
    def changeRole(cls, request):
        try:
            user: User = UserRepository.getUserByEmail(request['email'])
            if user is None:
                return Utils.createWrongResponse(False, Constants.NOT_FOUND, 404), 44
            else:
                UserRepository.changeRole(user, request['role'])
                if request['role'] == 'Member':
                    UserRepository.setAdmin(user, False)
                else:
                    UserRepository.setAdmin(user, True)
                return Utils.createSuccessResponse(True, Constants.CREATED)
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 400), 400
        
    @classmethod
    def addLike(cls, userId):
        UserRepository.addLike(userId)
        
    @classmethod
    def addQuestion(cls, userId):
        UserRepository.addQuestion(userId)
        
    @classmethod
    def addMessage(cls, userId):
        UserRepository.addMessage(userId)
    
    @classmethod
    def removeLike(cls, userId):
        UserRepository.removeLike(userId)

    @classmethod
    def removeMessage(cls, userId):
        UserRepository.removeMessage(userId)

    @classmethod
    def setBanned(cls, request):
        UserRepository.setBanned(request['user_id'], request['banned'])
        return Utils.createSuccessResponse(True, Constants.CREATED)

    @classmethod
    def isUpToDate(cls, requestUser):
        user: dict = cls.getUser(requestUser['user_id'])
        if user == requestUser:
            return Utils.createSuccessResponse(True, Constants.UP_TO_DATE)
        else:
            return Utils.createWrongResponse(False, Constants.NOT_UP_TO_DATE, 306), 306

