import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
        port=os.getenv("DB_PORT", "5432")
    )

def add_expenses(title,amount,category,user_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO expenses(title, amount, category,user_id) VALUES (%s, %s, %s,%s)",(title, amount, category,user_id))
    conn.commit()
    cursor.close()
    conn.close()


def get_expenses(user_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute('select id,title,amount,category from expenses where user_id=%s',(user_id,))
    expenses=cursor.fetchall()
    cursor.close()
    conn.close()
    return expenses

def delete_expenses(expense_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute('delete from expenses where id= %s',(expense_id,))
    conn.commit()
    cursor.close()
    conn.close()

def update_expenses(expense_id,title,amount,category):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute('update expenses set title=%s, amount=%s, category=%s where id=%s',(title,amount,category,expense_id))
    conn.commit()
    cursor.close()
    conn.close()

def get_expense(expense_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute('select id,title,amount,category from expenses where id=%s',(expense_id,))
    expense=cursor.fetchone()
    cursor.close()
    conn.close()
    return expense

def search_expense(search_term,user_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute('select id,title,amount,category from expenses where user_id=%s and (title ILIKE %s or category ILIKE %s)',(user_id,f'%{search_term}%',f'%{search_term}%'))
    expenses=cursor.fetchall()
    cursor.close()
    conn.close()
    return expenses 

def get_category_expenses(user_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute('select category,sum(amount) from expenses where user_id=%s group by category ORDER BY SUM(amount) DESC',(user_id,))
    category_expenses=cursor.fetchall()
    cursor.close()
    conn.close()
    return category_expenses

def create_user(username,password_hash):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute('insert into users(username,password) values(%s,%s)',(username,password_hash))
    conn.commit()
    cursor.close()
    conn.close()

def get_user_by_username(username):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute('select id,username,password from users where username ILIKE %s',(username,))
    user=cursor.fetchone()
    cursor.close()
    conn.close()
    return user