from models.category import CategoryModel
from flask_restful import Resource,reqparse

class Category(Resource):

    def get(self,name):

        category = CategoryModel.find_by_name(name)

        if category:
            return category.json()
        return {'message':"No category with the name of'{}' exists".format(name)}

    def post(self,name):

        if CategoryModel.find_by_name(name):
            return {'message':"A category with the name of '{}' already exists".format(name)}

        category = CategoryModel(name)

        try:
            category.save_to_db()
        except:
            return {'message':"An error occured while creating the category."}, 500

        return {'message': "Category '{}' was created".format(name)}, 201

    def delete(self,name):

        category = CategoryModel.find_by_name(name)

        if category:
            category.delete_from_db()
            
        return {'message':'Deleted the category'}

class CategoryList(Resource):
    def get(self):
        return{'Categories':list(map(lambda x: x.json(), CategoryModel.query.all()))}
