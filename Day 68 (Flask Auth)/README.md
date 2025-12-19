# Day 68 — Flask Auth

A focused exercise on user authentication with Flask, showcasing registration, login/logout, protected routes, and secure file delivery. Uses `Flask-Login`, `SQLAlchemy`, and password hashing via `Werkzeug`.

---

## Overview

This mini-app demonstrates core authentication flows:
- Creating users with hashed passwords
- Logging users in/out and tracking sessions
- Restricting access to pages and downloads for authenticated users only

Entrypoint: [Day 68 (Flask Auth)/main.py](Day%2068%20(Flask%20Auth)/main.py)

---

## Features

- **Registration:** Creates a user with a unique email and a salted PBKDF2 hash.
- **Login/Logout:** Session management via `Flask-Login`.
- **Protected Views:** `login_required` guards the secrets page and file downloads.
- **Flash Messages:** Friendly feedback for duplicate email or bad credentials.
- **File Delivery:** Serves a PDF from `static/files` only to logged-in users.

---

## Tech Stack

- **Backend:** Flask, Flask-Login, Flask-SQLAlchemy, Werkzeug security
- **Templates:** Jinja2 (`index.html`, `register.html`, `login.html`, `secrets.html`)
- **Database:** SQLite (`users.db`) via SQLAlchemy 2.0 typed ORM

---

## Project Structure

- **App:** [Day 68 (Flask Auth)/main.py](Day%2068%20(Flask%20Auth)/main.py)
- **Templates:** [Day 68 (Flask Auth)/templates](Day%2068%20(Flask%20Auth)/templates)
- **Static:** [Day 68 (Flask Auth)/static](Day%2068%20(Flask%20Auth)/static)
  - Cheat sheet: [Day 68 (Flask Auth)/static/files/cheat_sheet.pdf](Day%2068%20(Flask%20Auth)/static/files/cheat_sheet.pdf)

---

## Database Model

Defined in `main.py`:

- **`User`**
  - `id` (int, PK)
  - `email` (string, unique)
  - `password` (string, hashed)
  - `name` (string)

The database is auto-created on startup with `db.create_all()` inside the app context.

---

## Routes

- **`/`**: Home page.
- **`/register`**: Register a new user.
- **`/login`**: Login flow with credential validation.
- **`/logout`**: Logout current user.
- **`/secrets`**: Protected page; shows the logged-in user’s name.
- **`/download`**: Protected file download (serves a PDF from `static/files`).

---

## How It Works

- **Session & Identity:** `Flask-Login` manages sessions; `current_user` reflects who’s logged in.
- **Password Hashing:** `generate_password_hash(..., method='pbkdf2:sha256', salt_length=8)` stores secure hashes; `check_password_hash` verifies credentials.
- **Login Required:** The `@login_required` decorator enforces access to secrets and downloads.
- **File Serving:** `send_from_directory('static', path='files/cheat_sheet.pdf')` returns the PDF to authenticated users.
- **User Loader:** `@login_manager.user_loader` loads users by ID from the DB.

---

## Setup & Run

1. **Create a virtual environment**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. **Install dependencies**

```bash
pip install flask flask-login flask-sqlalchemy
```

3. **Run the app**

```bash
python "Day 68 (Flask Auth)/main.py"
```

- Open `http://127.0.0.1:5000/`.

4. **Try the flow**
- Register a new account.
- Login, then visit `/secrets` and `/download`.

---

## Security Notes

- **Secret Key:** Currently set in code (`SECRET_KEY = 'secret-key-goes-here'`). Prefer loading from environment for production.
- **Password Storage:** Uses salted PBKDF2 via Werkzeug — do not store plain passwords.
- **User Loader:** In production, `user_loader` should return `None` if not found rather than aborting, to avoid unexpected 404s in session loading.
- **Static Files:** Sensitive files should be outside public `static` and streamed with checks in real apps.

---

## What I Used & How I Built It

- **Flask App + SQLAlchemy:** Set up the app, DB config (`sqlite:///users.db`), and typed models.
- **Auth Flow:** Implemented register/login/logout using `Flask-Login` and secure password hashing.
- **Protected Routes:** Applied `@login_required` to sensitive views.
- **Templates & UX:** Added Jinja templates and `flash` messages for a smoother experience.
- **File Serving:** Demonstrated safe delivery of a file to authenticated users.

---

## Next Steps / Ideas

- **Environment Config:** Load `SECRET_KEY` and DB URI from `.env` using `python-dotenv`.
- **Forms:** Use Flask-WTF for form validation and CSRF.
- **Password Reset:** Add email-based reset flow.
- **Profile Page:** Let users update `name` and view account info.
- **Testing:** Add unit tests for auth flows and protected routes.
