from flask import Flask, render_template, request, redirect
from database import add_expenses, get_expenses, delete_expenses, update_expenses, get_expense, search_expense, get_category_expenses, create_user, get_user_by_username
from werkzeug.security import generate_password_hash, check_password_hash
from flask import session
import os

app=Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

@app.route("/",methods=["GET","POST"])
def home():
    if "user_id" not in session:
            return redirect("/login")
    if request.method== "POST":
        title=request.form["title"]
        amount=request.form["amount"]
        category=request.form['category']
        add_expenses(title,amount,category,session["user_id"])
    name=session.get('username')
    search = request.args.get("search")
    if search:
        expenses = search_expense(search,session["user_id"])
    else:
        expenses = get_expenses(session["user_id"])
    total_amount=sum(expense[2] for expense in expenses)
    category_expenses=get_category_expenses(session["user_id"])

    return render_template("home.html",name=name,expenses=expenses,total_amount=total_amount,search=search,category_expenses=category_expenses)

@app.route('/delete/<int:expense_id>')
def delete(expense_id):
    delete_expenses(expense_id)
    return redirect('/')

@app.route("/edit/<int:expense_id>", methods=["GET", "POST"])
def edit(expense_id):

    if request.method == "POST":
        title = request.form["title"]
        amount = request.form["amount"]
        category = request.form["category"]
        update_expenses(expense_id,title,amount,category)
        return redirect("/")

    expense = get_expense(expense_id)
    return render_template("edit.html",expense=expense)

@app.route('/register',methods=["GET","POST"])
def register():
    if request.method=="POST":
        username=request.form["username"]
        password=request.form["password"]
        password_hash=generate_password_hash(password)
        create_user(username,password_hash)
        return redirect('/')
    return render_template("register.html")

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
        username=request.form["username"]
        password=request.form["password"]
        user=get_user_by_username(username)
        if user and check_password_hash(user[2],password):
            session["user_id"] = user[0]
            session["username"]=username
            return redirect("/")
    return render_template("login.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

if __name__=="__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
