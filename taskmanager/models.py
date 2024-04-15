from taskmanager import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    tasks = db.relationship("Recipe", backref="category", cascade="all,delete",lazy=True)

    def __repr__(self):
        return self.category_name



class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(50), unique=True, nullable=False)
    recipe_description = db.Column(db.Text, nullable=False)
    preparing_time = db.Column(db.Time, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return "#{0} - Recipe: {1}".format(
            self.id, self.recipe_name, self.preparing_time
        )






    


