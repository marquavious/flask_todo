from flask import Flask,jsonify,request
from flask_restful import Api, reqparse


app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'


from resources.todo import Todo, TodoList

@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Todo,'/todo/<string:title>')
api.add_resource(TodoList,'/todos')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000,debug=True)
