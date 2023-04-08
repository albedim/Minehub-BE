from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import cross_origin
from minehub.service.UserService import UserService
from minehub.utils.Utils import Utils


user: Blueprint = Blueprint('UserController', __name__, url_prefix=Utils.getURL('user'))


@user.route("/signin", methods=['POST'])
@cross_origin()
def signin():
    return UserService.signin(request.json)


@user.route("/sync", methods=['GET'])
@cross_origin()
@jwt_required()
def isExpired():
    return UserService.sync(get_jwt_identity())


@user.route("/password_forgotten_token/<email>", methods=['PUT'])
@cross_origin()
def createPasswordForgottenToken(email):
    return UserService.createForgottenPasswordToken(email)


@user.route("/password_forgotten_token/<token>", methods=['GET'])
@cross_origin()
def getUserByPasswordForgottenToken(token):
    return UserService.getUserByPasswordForgottenToken(token)


@user.route("/change_password", methods=['PUT'])
@cross_origin()
def changePassword():
    return UserService.changePassword(request.json)


@user.route("/get/<userId>", methods=['GET'])
@cross_origin()
def get(userId):
    return UserService.getUser(userId)


@user.route("/signup", methods=['POST'])
@cross_origin()
def signup():
    return UserService.signup(request.json)


@user.route("/get/staffers", methods=['GET'])
@cross_origin()
def getStaffers():
    return UserService.getStaffers()


@user.route("/get/recent", methods=['GET'])
@cross_origin()
def getRecent():
    return UserService.getRecent()


@user.route("/admin", methods=['POST'])
@cross_origin()
def admin():
    return UserService.admin(request.json)


@user.route("/change/role", methods=['PUT'])
@cross_origin()
def changeRole():
    return UserService.changeRole(request.json)


@user.route("/change", methods=['PUT'])
@cross_origin()
def change():
    return UserService.change(request.json)


@user.route("/ban", methods=['PUT'])
@cross_origin()
def ban():
    return UserService.setBanned(request.json)



