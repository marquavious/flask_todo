from db import db

class TodoModel(db.Model):

    __tablename__ = 'todos'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    category_id = db.Column(db.String,db.ForeignKey('categories.name'))
    category = db.relationship('CategoryModel')

    def __init__(self,title,description, category_id):
        self.title = title
        self.description = description
        self.category_id = category_id

    def __str__(self):
        return self.title

    def json(self):
        return { 'name':self.title, 'description':self.description, 'category_name':self.category_id }

    @classmethod
    def find_by_title(cls,title):
        return cls.query.filter_by(title=title).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
