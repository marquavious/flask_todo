from models.todo import TodoModel
from flask_restful import Resource,reqparse

class Category(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('title',
        type = str,
        required = True,
        help="Every Category must have a name!"
    )

    def __init__(self,name):
        self.name = name

    def get():
        pass

    def post():
        pass

    def put():
        pass

    def delete():
        pass
