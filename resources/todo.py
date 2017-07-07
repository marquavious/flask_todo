from models.todo import TodoModel
from flask_restful import Resource,reqparse

class Todo(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('description',
        type = str,
        required = True,
        help = "All todos must have a description"
    )

    parser.add_argument('category',
        type = str,
        required = True,
        help = "All todos must be placed in a category"
    )

    def get(self,title):

        todo = TodoModel.find_by_title(title)

        if todo:
            return todo.json()

        return {'message':'Note was never created'}

    def post(self,title):

        if TodoModel.find_by_title(title):
             return {"message":"A todo with the title of '{}' already exists.".format(title)}

        data = Todo.parser.parse_args()
        todo = TodoModel(title,data['description'],data['category'])

        try:
            todo.save_to_db()
        except:
            return {'message':'Error saving todo'}, 500

        return todo.json(), 201

    def put(self,title):

        data = Todo.parser.parse_args()
        todo = TodoModel.find_by_title(title)

        if todo is None:
            todo = TodoModel(title,data['description'],data['description'])
        else:
            todo.description = data['description']
            todo.category_id = data['category']

        try:
            todo.save_to_db()
        except:
            return {'message':'Error updating todo'}, 500

        return todo.json()

    def delete(self,title):

        todo = TodoModel.find_by_title(title)

        if todo:
            todo.delete_from_db()

        return {'message':'todo deleted'}

class TodoList(Resource):
    def get(self):
        return {'todos':[x.json() for x in TodoModel.query.all()]}
