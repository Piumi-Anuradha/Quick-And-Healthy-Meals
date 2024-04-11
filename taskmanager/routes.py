from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Recipe


@app.route("/")
def home():
    return render_template("recipes.html")