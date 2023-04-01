from flask import jsonify

from minehub.model.entity.Category import Category
from minehub.model.entity.Message import Message
from minehub.model.entity.Question import Question
from minehub.model.repository.CategoryRepository import CategoryRepository
from minehub.model.repository.QuestionRepository import QuestionRepository
from minehub.service.MessageService import MessageService
from minehub.utils.Constants import Constants
from minehub.utils.Utils import Utils


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 05/03/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the server service
#


class CategoryService():

    @classmethod
    def getCategories(cls):
        categories: list[Category] = CategoryRepository.getCategories()
        result: list[dict] = []
        for category in categories:
            questions: list[Question] = QuestionRepository.getQuestionsByCategory(category.category_id)
            messages: list[Message] = MessageService.getMessagesByCategory(category.category_id)
            result.append(category.toJson_Questions_Messages(len(questions), len(messages)))
        return jsonify(result)

    @classmethod
    def get(cls, categoryId):
        return CategoryRepository.get(categoryId).toJson()

    @classmethod
    def add(cls, request):
        try:
            CategoryRepository.add(request['name'], request['editable'], request['private'])
            return Utils.createSuccessResponse(True, Constants.CREATED)
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 400), 400