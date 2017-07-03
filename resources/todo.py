from models.todo import TodoModel
from flask_restful import Resource,reqparse


class Todo(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('title',
        type = str,
        required = True,
        help = "All todos must have a title"
    )

    parser.add_argument('description',
        type = str,
        required = True,
        help = "All todos must have a description"
    )

    def get(self,title):
        todo = TodoModel.find_by_title(title)
        if todo:
            return todo.json()
        return {'message':'Note was never created'}

    def post(self,title):
        # if TodoModel.find_by_title(title):
        #      return {"message':'a todo with the title of '{}' already exists.".format(title)}

        data = Todo.parser.parse_args()

        todo = TodoModel(title,data['description'])

        try:
            todo.save_to_db()
        except:
            return {'message':'Error saving todo to firebase'}, 500

        return todo.json(), 201

    def put(self,title):
         # Grab data from parser
        data = Todo.parser.parse_args()

        # Look for an item
        todo = TodoModel.find_by_title(title)

        # If the item doesnt exists, create one
        if todo is None:
            todo = TodoModel(title,data['description'])
        # Else just update price
        else:
            todo.description = data['description']

        # Save it or update it to the DB
        todo.save_to_db()

        # Return json of the item to show it was created
        return todo.json()

    def delete(self,title):
        todo = TodoModel.find_by_title(title)

        if todo:
            todo.delete_from_db()

        return {'message':'todo delted'}

class TodoList(Resource):
    def get(self):
        return {'todos':[x.json() for x in TodoModel.query.all()]}
