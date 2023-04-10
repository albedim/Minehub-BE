from flask import Blueprint, request
from flask_cors import cross_origin
from flask_jwt_extended import get_jwt_identity, jwt_required

from minehub.service.CategoryService import CategoryService
from minehub.utils.Utils import Utils


category: Blueprint = Blueprint('CategoryController', __name__, url_prefix=Utils.getURL('category'))


@category.route("/get", methods=['GET'])
@cross_origin()
def get():
    return CategoryService.getCategories()


@category.route("/add", methods=['POST'])
@cross_origin()
def add():
    return CategoryService.add(request.json)


@category.route("/remove/<categoryId>", methods=['DELETE'])
@jwt_required()
@cross_origin()
def remove(categoryId: int):
    return CategoryService.remove(get_jwt_identity()['user_id'], categoryId)