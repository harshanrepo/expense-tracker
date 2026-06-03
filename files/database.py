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
    )

def add_expenses(title,amount,category):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO expenses(title, amount, category) VALUES (%s, %s, %s)",(title, amount, category))
    conn.commit()
    cursor.close()
    conn.close()

def get_expenses():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute('select id,title,amount,category from expenses')
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