from db import db

class CategoryModel(db.Model):

    __tablename__= "category"

    name = db.Column(db.String)
    id = db.Column(db.Integer, primary_key=True)
    todos = db.Relationship('TodoModel', lazy = 'dynamic')


    def __init__(self,name):
        self.name = name

    def json(self):
        return {'name':self.name,'items':[todo.json() for todo in self.todos]}

    @classmethod
    def find_by_name(cls,name):
        return cls.query.find_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
