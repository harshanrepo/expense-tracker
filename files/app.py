from flask import Flask, render_template, request, redirect
from database import add_expenses, get_expenses, delete_expenses,update_expenses,get_expense
expenses=[]

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method== "POST":
        title=request.form["title"]
        amount=request.form["amount"]
        category=request.form['category']
        add_expenses(title,amount,category)
    expenses = get_expenses()

    return render_template("home.html",name="Reen",expenses=expenses)

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

@app.route("/about")
def about():
    return render_template("about.html")


if __name__=="__main__":
    app.run(debug=True)
