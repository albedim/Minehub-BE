from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import cross_origin
from minehub.service.question.QuestionService import QuestionService
from minehub.utils.Utils import Utils


question: Blueprint = Blueprint('QuestionController', __name__, url_prefix=Utils.getURL('question'))


@question.route("/get/<categoryId>/category", methods=['GET'])
@cross_origin()
@jwt_required()
def getQuestionsByCategory(categoryId):
    return QuestionService.getQuestionsByCategory(get_jwt_identity()['user_id'], categoryId)


@question.route('/get/<questionId>', methods=['GET'])
@cross_origin()
@jwt_required()
def get(questionId):
    return QuestionService.get(get_jwt_identity()['user_id'], questionId)


@question.route("/add", methods=['POST'])
@cross_origin()
def add():
    return QuestionService.add(request.json)


@question.route("/change/status", methods=['PUT'])
@jwt_required()
@cross_origin()
def changeStatus():
    return QuestionService.changeStatus(request.json)


@question.route("/remove/<questionId>", methods=['DELETE'])
@jwt_required()
@cross_origin()
def remove(questionId: int):
    return QuestionService.remove(get_jwt_identity()['user_id'], questionId)





