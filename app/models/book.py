from app import db

class Book(db.Model): #the class Book inherits db.Model from SQLAchemy
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
