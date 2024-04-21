from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Recipe


@app.route("/")
def home():
    return render_template("recipes.html")


@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html",categories = categories)


@app.route("/add_category", methods=["GET","POST"])
def add_category():
    if request.method=="POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")


@app.route("/edit_category/<int:category_id>", methods=["GET","POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))


@app.route("/add_recipes", methods=["GET","POST"])
def add_recipes():
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method=="POST":
        task = Recipe(
            recipe_name = request.form.get("recipe_name"),
            recipe_description = request.form.get("recipe_description"),
            preparing_time = request.form.get("preparing_time"),
            category_id = request.form.get("category_id")
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_recipes.html",categories=categories)