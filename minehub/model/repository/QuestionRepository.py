from sqlalchemy import desc
from minehub.configuration.config import sql
from minehub.model.entity.Question import Question


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 06/03/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the d service
#

class QuestionRepository():

    @classmethod
    def getQuestionsByCategory(cls, categoryId):
        questions: list[Question] = sql.session.query(Question).filter(Question.category_id == categoryId)\
            .order_by(desc(Question.created_on)).all()
        return questions

    @classmethod
    def getAllQuestions(cls):
        questions: list[Question] = sql.session.query(Question).all()
        return questions

    @classmethod
    def get(cls, questionId):
        question: Question = sql.session.query(Question).filter(Question.question_id == questionId).first()
        return question

    @classmethod
    def getQuestionsByCategoryOf(cls, userId, categoryId):
        questions: list[Question] = sql.session.query(Question).filter(Question.category_id == categoryId).filter(Question.owner_id == userId)\
            .order_by(desc(Question.created_on)).all()
        return questions

    @classmethod
    def add(cls, name, ownerId, categoryId):
        question: Question = Question(name, ownerId, categoryId)
        sql.session.add(question)
        sql.session.commit()

    @classmethod
    def changeStatus(cls, questionId, status):
        question: Question = cls.get(questionId)
        question.status = status
        sql.session.commit()

    @classmethod
    def setClosed(cls, questionId, status):
        question: Question = cls.get(questionId)
        question.closed = status
        sql.session.commit()

    @classmethod
    def getLastQuestion(cls, ownerId):
        question: Question = sql.session.query(Question).filter(Question.owner_id == ownerId).order_by(desc(Question.question_id)).first()
        return question

    @classmethod
    def remove(cls, questionId):
        question: Question = sql.session.query(Question).filter(Question.question_id == questionId).delete()
        sql.session.commit()

    @classmethod
    def removeQuestions(cls, categoryId):
        question: list[Question] = sql.session.query(Question).filter(Question.category_id == categoryId).delete()
        sql.session.commit()