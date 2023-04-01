from minehub.configuration.config import sql

#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 05/03/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the category entity
#


class Category(sql.Model):
    __tablename__ = 'categories'
    category_id: int = sql.Column(sql.Integer, primary_key=True)
    editable: bool = sql.Column(sql.Boolean, nullable=False)
    private: bool = sql.Column(sql.Boolean, nullable=False)
    name: str = sql.Column(sql.String(40), nullable=False)

    def __init__(self, name, editable, private):
        self.name = name
        self.editable = editable
        self.private = private

    def toJson(self):
        return {
            'category_id': self.category_id,
            'editable': self.editable,
            'name': self.name,
            'private': self.private
        }

    def toJson_Questions_Messages(self, questions, messages):
        return {
            'category_id': self.category_id,
            'name': self.name,
            'editable': self.editable,
            'private': self.private,
            'questions': questions,
            'messages': messages
        }