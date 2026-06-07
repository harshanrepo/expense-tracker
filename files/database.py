import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


# ── Connection factory ─────────────────────────────────────────────
def get_connection():
    """Create and return a new PostgreSQL connection using env vars."""
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT", "5432")
    )


# ── Expenses CRUD ──────────────────────────────────────────────────
def add_expenses(title, amount, category, user_id):
    """Insert a new expense row for the given user."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO expenses (title, amount, category, user_id) VALUES (%s, %s, %s, %s)",
                (title, amount, category, user_id)
            )


def get_expenses(user_id):
    """Fetch all expenses for a user, newest first."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT id, title, amount, category FROM expenses WHERE user_id = %s ORDER BY id DESC",
                (user_id,)
            )
            return cursor.fetchall()


def delete_expenses(expense_id):
    """Delete a single expense by its ID."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM expenses WHERE id = %s", (expense_id,))


def update_expenses(expense_id, title, amount, category):
    """Update title, amount, and category for a given expense."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE expenses SET title = %s, amount = %s, category = %s WHERE id = %s",
                (title, amount, category, expense_id)
            )


def get_expense(expense_id):
    """Fetch a single expense row by ID."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT id, title, amount, category FROM expenses WHERE id = %s",
                (expense_id,)
            )
            return cursor.fetchone()


def search_expense(search_term, user_id):
    """Search expenses by title or category (case-insensitive)."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """SELECT id, title, amount, category FROM expenses
                   WHERE user_id = %s AND (title ILIKE %s OR category ILIKE %s)""",
                (user_id, f"%{search_term}%", f"%{search_term}%")
            )
            return cursor.fetchall()


def get_category_expenses(user_id):
    """Return total spending per category for a user, highest first."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """SELECT category, SUM(amount) FROM expenses
                   WHERE user_id = %s GROUP BY category ORDER BY SUM(amount) DESC""",
                (user_id,)
            )
            return cursor.fetchall()


# ── Users ──────────────────────────────────────────────────────────
def create_user(username, password_hash):
    """Insert a new user with a hashed password."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                (username, password_hash)
            )


def get_user_by_username(username):
    """Fetch a user row by username (case-insensitive)."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT id, username, password FROM users WHERE username ILIKE %s",
                (username,)
            )
            return cursor.fetchone()