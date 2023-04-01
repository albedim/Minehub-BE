from flask import Blueprint, request
from flask_cors import cross_origin
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