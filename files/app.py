from flask import Flask, render_template, request, redirect, session, flash
from files.database import (
    add_expenses, get_expenses, delete_expenses,
    update_expenses, get_expense, search_expense,
    get_category_expenses, create_user, get_user_by_username
)
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


# ── Auth guard helper ──────────────────────────────────────────────
def login_required():
    """Returns a redirect if the user is not logged in, else None."""
    if "user_id" not in session:
        return redirect("/login")
    return None


# ── Home / Dashboard ───────────────────────────────────────────────
@app.route("/", methods=["GET", "POST"])
def home():
    guard = login_required()
    if guard:
        return guard

    if request.method == "POST":
        title    = request.form["title"]
        amount   = request.form["amount"]
        category = request.form["category"]
        add_expenses(title, amount, category, session["user_id"])
        return redirect("/")          # PRG pattern — prevents duplicate submit on refresh

    name   = session.get("username")
    search = request.args.get("search", "").strip()

    # Use search query if present, otherwise fetch all
    expenses = search_expense(search, session["user_id"]) if search else get_expenses(session["user_id"])

    total_amount      = sum(e[2] for e in expenses)
    category_expenses = get_category_expenses(session["user_id"])

    return render_template(
        "home.html",
        name=name,
        expenses=expenses,
        total_amount=total_amount,
        search=search,
        category_expenses=category_expenses
    )


# ── Delete expense ─────────────────────────────────────────────────
@app.route("/delete/<int:expense_id>")
def delete(expense_id):
    guard = login_required()
    if guard:
        return guard                  # Prevent unauthenticated deletes
    delete_expenses(expense_id)
    return redirect("/")


# ── Edit expense ───────────────────────────────────────────────────
@app.route("/edit/<int:expense_id>", methods=["GET", "POST"])
def edit(expense_id):
    guard = login_required()
    if guard:
        return guard                  # Prevent unauthenticated edits

    if request.method == "POST":
        title    = request.form["title"]
        amount   = request.form["amount"]
        category = request.form["category"]
        update_expenses(expense_id, title, amount, category)
        return redirect("/")

    expense = get_expense(expense_id)
    return render_template("edit.html", expense=expense)


# ── Register ───────────────────────────────────────────────────────
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        # Check for duplicate username before inserting
        if get_user_by_username(username):
            return render_template("register.html", error="Username already taken.")

        password_hash = generate_password_hash(password)
        create_user(username, password_hash)

        # Auto-login after registration
        user = get_user_by_username(username)
        session["user_id"]  = user[0]
        session["username"] = username
        return redirect("/")

    return render_template("register.html")


# ── Login ──────────────────────────────────────────────────────────
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]
        user     = get_user_by_username(username)

        if user and check_password_hash(user[2], password):
            session["user_id"]  = user[0]
            session["username"] = username
            return redirect("/")

        # Pass error message to template
        return render_template("login.html", error="Invalid username or password.")

    return render_template("login.html")


# ── About ──────────────────────────────────────────────────────────
@app.route("/about")
def about():
    guard = login_required()
    if guard:
        return guard
    name = session.get("username")
    return render_template("about.html", name=name)


# ── Logout ─────────────────────────────────────────────────────────
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


# ── Entry point ────────────────────────────────────────────────────
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)