from minehub.model.repository.CategoryRepository import CategoryRepository
from minehub.model.repository.QuestionRepository import QuestionRepository
from minehub.model.repository.UserRepository import UserRepository


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 06/03/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the user service
#


class UserPermissionsService():

    @classmethod
    def hasCategoryAccess(cls, userId, categoryId):
        if CategoryRepository.get(categoryId).private:
            if cls.isStaffer(userId):
                return "ALL"
            else:
                return "OWN"
        else:
            return "ALL"

    @classmethod
    def hasQuestionAccess(cls, userId, questionId):
        question = QuestionRepository.get(questionId)
        if CategoryRepository.get(question.category_id).private:
            if cls.isStaffer(userId) or QuestionRepository.get(questionId).owner_id == userId:
                return True
            else:
                return False
        else:
            return True

    @classmethod
    def isStaffer(cls, userId) -> bool:
        return UserRepository.getUserById(userId).admin
