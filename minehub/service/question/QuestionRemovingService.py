from minehub.model.entity.Question import Question
from minehub.model.repository.MessageRepository import MessageRepository
from minehub.model.repository.QuestionRepository import QuestionRepository
from minehub.utils.Constants import Constants
from minehub.utils.Utils import Utils


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 10/04/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the question removing service
#

class QuestionRemovingService():

    @classmethod
    def removeQuestions(cls, categoryId):
        questions: list[Question] = QuestionRepository.getQuestionsByCategory(categoryId)
        for question in questions:
            QuestionRepository.remove(question.question_id)
            MessageRepository.removeMessages(question.question_id)
        return Utils.createSuccessResponse(True, Constants.CREATED)

