💸 Expense Tracker

> 🚧 Currently in progress

A web-based Expense Tracker built with Flask and PostgreSQL.
This project is part of my Python backend development journey,
focusing on real-world CRUD operations and database integration.

---

✨ Features (so far)

- Add expenses with title, amount and category
- View all expenses on homepage
- Delete expenses
- Data stored in PostgreSQL database

---

🛠️ Tech Stack

- **Language:** Python 3
- **Framework:** Flask
- **Database:** PostgreSQL
- **Frontend:** HTML, Jinja2 Templates
- **Concepts:** REST routes, OOP, CRUD operations

---

📂 Project Structure

expense-tracker/
├── files/
│   ├── templates/
│   │   ├── home.html
│   │   └── about.html
│   ├── app.py
│   └── database.py
├── .env
├── .gitignore
└── venv/

---

🚀 How to Run

1. Clone the repo
2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```
3. Install dependencies
```bash
pip install flask psycopg2-binary python-dotenv
```
4. Add your PostgreSQL credentials in `.env`
5. Run the app
```bash
python files/app.py
```

---

🔮 Planned Features

- [ ] Edit existing expenses
- [ ] Filter by category
- [ ] Monthly summary / charts
- [ ] User login system

---

👨‍💻 Author

**Harshan** | CSE Student | Chennai
🔗 [LinkedIn](https://linkedin.com/in/mrshri-harshan) |
🐙 [GitHub](https://github.com/harshanrepo)
