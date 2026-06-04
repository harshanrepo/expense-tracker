# 💸 SpendWise — Expense Tracker

A full-stack web application to track your daily expenses, built with
Flask and PostgreSQL. Features a clean UI with user authentication,
category breakdown, and real-time search.

---

## ✨ Features

- 🔐 User Registration & Login (with password hashing)
- ➕ Add expenses with title, amount and category
- ✏️ Edit & Delete expenses
- 🔍 Search by title or category
- 📊 Category-wise breakdown with visual progress bars
- 💰 Total spent & transaction count dashboard
- 🚪 Session-based authentication with Logout

---

## 🛠️ Tech Stack

| Layer | Tech |
|-------|------|
| Backend | Python, Flask |
| Database | PostgreSQL |
| Frontend | HTML, CSS, Jinja2 |
| Auth | Werkzeug (password hashing) |
| Fonts | Google Fonts (DM Sans, Syne) |

---

## 📂 Project Structure
expense-tracker/
├── files/
├── .gitignore
└── README.md

---

## 🚀 How to Run

1. Clone the repo
```bash
git clone https://github.com/harshanrepo/expense-tracker.git
cd expense-tracker
```

2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies
```bash
pip install flask psycopg2-binary python-dotenv werkzeug
```

4. Create a `.env` file with your PostgreSQL credentials
DB_HOST=localhost
DB_NAME=your_db_name
DB_USER=your_username
DB_PASSWORD=your_password

5. Run the app
```bash
python files/app.py
```

---

## 🔮 Planned Features

- [ ] Monthly expense summary
- [ ] Charts and analytics
- [ ] Export to CSV
- [ ] Budget limit alerts

---

## 👨‍💻 Author

**Shri Harshan M** | CS Graduate | Chennai
🔗 [LinkedIn](https://linkedin.com/in/mrshri-harshan) |
🐙 [GitHub](https://github.com/harshanrepo)
