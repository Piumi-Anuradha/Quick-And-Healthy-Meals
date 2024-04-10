from taskmanager import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)

    def __repr__(self):
        return self.category_name



class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.Integer(50), unique=True, nullable=True)

    def __repr__(self):
        return self


