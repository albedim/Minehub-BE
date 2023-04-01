from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import cross_origin
from minehub.service.MessageService import MessageService
from minehub.utils.Utils import Utils


message: Blueprint = Blueprint('MessageController', __name__, url_prefix=Utils.getURL('message'))


@message.route("/get/<questionId>/question", methods=['GET'])
@cross_origin()
@jwt_required()
def get(questionId):
    return MessageService.getMessages(get_jwt_identity()['user_id'], questionId)


@message.route("/add", methods=['POST'])
@cross_origin()
def add():
    return MessageService.add(request.json)


@message.route("/remove/<messageId>", methods=['DELETE'])
@cross_origin()
@jwt_required()
def remove(messageId):
    return MessageService.removeMessage(get_jwt_identity(), messageId)


@message.route("/change", methods=['PUT'])
@cross_origin()
def changeMessage():
    return MessageService.changeMessage(request.json)


