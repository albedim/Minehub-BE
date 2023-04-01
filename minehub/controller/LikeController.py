from flask import Blueprint, request
from flask_cors import cross_origin
from minehub.service.LikeService import LikeService
from minehub.utils.Utils import Utils


like: Blueprint = Blueprint('LikeController', __name__, url_prefix=Utils.getURL('like'))


@like.route("/add", methods=['POST'])
@cross_origin()
def add():
    return LikeService.add(request.json)


@like.route("/remove", methods=['DELETE'])
@cross_origin()
def remove():
    return LikeService.remove(request.args.get("user_id"), request.args.get("message_id"))


