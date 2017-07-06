from models.todo import TodoModel
from flask_restful import Resource,reqparse

class Category(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('name',
        type = str,
        required = True,
        help="Every Category must have a name!"
    )

    def __init__(self,name):
        self.name = name

    def get(self,name):
        category = CategoryModel.find_by_name(name)

        if category:
            return category.json()
        return {'message':"No category with the name of'{}' exists".format(name)}

    def post(self,name):
        if CategoryModel.find_by_name(name):
            return {'message':"A category with the name of '{}' already exists".format(name)}

        data = parser.parse_args()

        category = CategoryModel(data["name"])

        try:
            category.save_to_db()
        except:
            return {'message':"A error occured wil creating the category."}, 500

        return {'message': "Category '{}' was created".format(name)}, 201

    def delete(self,name):
        category = Category.find_by_name(name)
        if category:
            category.delete_from_db()
        return {'message':'Deleted the category'}

class CategoryList(Resource):
    def get(self):
        return{'Categories':list(map(lambda x: x.json(), in CategoryModel.query.all()))}
