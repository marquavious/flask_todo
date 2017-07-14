from flask import Flask,jsonify,request
from flask_restful import Api, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from resources.category import Category,CategoryList
from resources.todo import Todo, TodoList
from models.todo import TodoModel
from models.category import CategoryModel
from db import db
from flask import Flask
from flask_restful import Resource, Api, reqparse
import werkzeug

app = Flask(__name__)
api = Api(app)

admin = Admin(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'

api.add_resource(Todo,'/todo/<string:title>')
api.add_resource(TodoList,'/todos')
api.add_resource(Category,'/category/<string:name>')
api.add_resource(CategoryList, '/categories')

@app.before_first_request
def create_tables():
    db.create_all()

admin.add_view(ModelView(TodoModel, db.session))
admin.add_view(ModelView(CategoryModel, db.session))

class UploadAudio(Resource):
  def post(self):
    parse = reqparse.RequestParser()
    parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
    args = parse.parse_args()
    audioFile = args['file']
    audioFile.save("your_file_name.jpg")

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000,debug = True)
