from flask import jsonify
from minehub.model.entity.Question import Question
from minehub.model.repository.MessageRepository import MessageRepository
from minehub.model.repository.QuestionRepository import QuestionRepository
from minehub.service.CategoryService import CategoryService
from minehub.service.users.UserPermissionsService import UserPermissionsService
from minehub.service.users.UserService import UserService
from minehub.utils.Constants import Constants
from minehub.utils.Utils import Utils


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 06/03/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the question service
#

class QuestionService():

    @classmethod
    def getQuestionsByCategory(cls, userId, categoryId):
        permissions = UserPermissionsService.hasCategoryAccess(userId, categoryId)
        category: dict = CategoryService.get(categoryId)
        questions: list = []
        result: dict = {'category': category, 'questions': []}
        if permissions == 'OWN':
            questions: list[Question] = QuestionRepository.getQuestionsByCategoryOf(userId, categoryId)
        elif permissions == 'ALL':
            questions: list[Question] = QuestionRepository.getQuestionsByCategory(categoryId)
        for question in questions:
            owner: dict = UserService.getUser(question.owner_id)
            messages: list = MessageRepository.getMessages(question.question_id)
            result['questions'].append(question.toJson_Owner_Messages(owner, len(messages)))
        return jsonify(result)

    @classmethod
    def getAllQuestions(cls):
        questions: list[Question] = QuestionRepository.getAllQuestions()
        return Utils.createList(questions)

    @classmethod
    def get(cls, userId, questionId):
        permissions: bool = UserPermissionsService.hasQuestionAccess(userId, questionId)
        if permissions:
            question: Question = QuestionRepository.get(questionId)
            owner = UserService.getUser(question.owner_id)
            return question.toJson_Owner(owner)
        else:
            return Utils.createWrongResponse(False, Constants.NOT_ENOUGH_PERMISSIONS, 403), 403

    @classmethod
    def exists(cls, questionId):
        return QuestionRepository.get(questionId) is not None

    @classmethod
    def add(cls, request):
        try:
            QuestionRepository.add(request['name'], request['owner_id'], request['category_id'])
            UserService.addQuestion(request['owner_id'])
            return Utils.createSuccessResponse(True, QuestionRepository.getLastQuestion(request['owner_id']).question_id)
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 400), 400

    @classmethod
    def changeStatus(cls, request):
        try:
            QuestionRepository.changeStatus(request['question_id'], request['status'])
            if request['status'] == 'accepted' or request['status'] == 'rejected':
                QuestionRepository.setClosed(request['question_id'], True)
            else:
                QuestionRepository.setClosed(request['question_id'], False)
            return Utils.createSuccessResponse(True, Constants.CREATED)
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 400), 400

    @classmethod
    def remove(cls, userId, questionId):
        if cls.exists(questionId):
            if UserPermissionsService.isStaffer(userId) or QuestionRepository.get(questionId).owner_id == userId:
                QuestionRepository.remove(questionId)
                MessageRepository.removeMessages(questionId)
                LikeService.removeLikes()
                return Utils.createSuccessResponse(True, Constants.CREATED)
            else:
                return Utils.createWrongResponse(False, Constants.NOT_ENOUGH_PERMISSIONS, 403), 403
        else:
            return Utils.createWrongResponse(False, Constants.NOT_ENOUGH_PERMISSIONS, 403), 403
