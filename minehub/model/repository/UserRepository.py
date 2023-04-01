from sqlalchemy import desc
from minehub.configuration.config import sql
from minehub.model.entity.User import User


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 05/03/23
# Created at: 19:35
# Version: 1.0.0
# Description: This is the class for the user repository
#

class UserRepository():

    @classmethod
    def signin(cls, email, password) -> User:
        user: User = sql.session.query(User).filter(User.email == email).filter(User.password == password).first()
        return user

    @classmethod
    def signup(cls, name, email, minecraftUsername, password) -> None:
        user: User = User(name, email, minecraftUsername, password)
        sql.session.add(user)
        sql.session.commit()

    @classmethod
    def getUserById(cls, userId) -> User:
        user: User = sql.session.query(User).filter(User.user_id == userId).first()
        return user

    @classmethod
    def getUserByEmail(cls, email):
        user: User = sql.session.query(User).filter(User.email == email).first()
        return user

    @classmethod
    def getUserByMinecraftUsername(cls, minecraftUsername):
        user: User = sql.session.query(User).filter(User.minecraft_username == minecraftUsername).first()
        return user

    @classmethod
    def createForgottenPasswordToken(cls, user, token):
        user.password_forgotten_token = token
        sql.session.commit()

    @classmethod
    def getUserByPasswordForgottenToken(cls, token):
        user: User = sql.session.query(User).filter(User.password_forgotten_token == token).first()
        return user

    @classmethod
    def changePassword(cls, userId, newPassword):
        user: User = cls.getUserById(userId)
        user.password = newPassword
        sql.session.commit()

    @classmethod
    def getStaffers(cls):
        users: list[User] = sql.session.query(User).filter(User.admin == True).all()
        return users

    @classmethod
    def getAllUsers(cls):
        users: list[User] = sql.session.query(User).all()
        return users

    @classmethod
    def getRecent(cls):
        users: list[User] = sql.session.query(User).order_by(desc(User.messages)).limit(10).all()
        return users

    @classmethod
    def addLike(cls, userId):
        user: User = cls.getUserById(userId)
        user.likes += 1
        sql.session.commit()
        
    @classmethod
    def addQuestion(cls, userId):
        user: User = cls.getUserById(userId)
        user.questions += 1
        sql.session.commit()
              
    @classmethod
    def addMessage(cls, userId):
        user: User = cls.getUserById(userId)
        user.messages += 1
        sql.session.commit()

    @classmethod
    def removeLike(cls, userId):
        user: User = cls.getUserById(userId)
        user.likes -= 1
        sql.session.commit()

    @classmethod
    def removeMessage(cls, userId):
        user: User = cls.getUserById(userId)
        user.messages -= 1
        sql.session.commit()

    @classmethod
    def changeRole(cls, user, role_id):
        user.role_id = role_id
        sql.session.commit()

    @classmethod
    def setAdmin(cls, user, admin):
        user.admin = admin
        sql.session.commit()

    @classmethod
    def setBanned(cls, userId, banned):
        user: User = cls.getUserById(userId)
        user.banned = banned
        sql.session.commit()

    @classmethod
    def change(cls, user, name, minecraftUsername, email):
        user.name = name
        user.minecraft_username = minecraftUsername
        user.email = email
        sql.session.commit()
