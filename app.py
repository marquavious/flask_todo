from flask import Flask,jsonify,request
from flask_restful import Api, reqparse
from resources.category import Category,CategoryList
from resources.todo import Todo, TodoList

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api.add_resource(Todo,'/todo/<string:title>')
api.add_resource(TodoList,'/todos')
api.add_resource(Category,'/category/<string:name>')
api.add_resource(CategoryList, '/categories')

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000)
