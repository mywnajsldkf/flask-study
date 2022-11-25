from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Plan(db.Model):
    __tablename__ = "plan"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(32))
    description = db.Column(db.String(100))
    when = db.Column(db.String(30))
    who = db.Column(db.String(10))
    where = db.Column(db.String(30))

    def obj_to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "when": self.when,
            "who": self.who,
            "where": self.where 
        }

    def __init__(self, title, description, when, who, where):
        self.title = title
        self.description = description
        self.when = when
        self.who = who
        self.where = where        