# Flask Authentication System

A complete user authentication system built with Flask that demonstrates modern security practices including password hashing, session management, protected routes, and secure file delivery.

## Features

- **User Registration**: Create new accounts with email validation and duplicate checking
- **Secure Login**: Authenticate users with hashed password verification
- **Session Management**: Track user sessions with Flask-Login
- **Protected Routes**: Restrict access to authenticated users only
- **File Downloads**: Secure file delivery for logged-in users
- **Flash Messages**: User-friendly feedback for registration and login actions
- **Auto-logout**: Session cleanup on logout
- **Password Security**: PBKDF2 hashing with salt for secure password storage

## Pages/Routes

- **Home Page** (`/`): Landing page accessible to all users
- **Register** (`/register`): User registration form with validation
- **Login** (`/login`): User authentication form
- **Secrets** (`/secrets`): Protected page displaying user information (requires login)
- **Download** (`/download`): Protected file download endpoint (requires login)
- **Logout** (`/logout`): Terminates user session and redirects to home

## How to Use

1. Install required dependencies:
   ```bash
   pip install flask flask-login flask-sqlalchemy werkzeug
   ```

2. Run the application:
   ```bash
   python main.py
   ```

3. Navigate to `http://127.0.0.1:5000` in your browser

4. Register a new account with your name, email, and password

5. Login with your credentials to access protected pages

6. Visit `/secrets` to see your personalized page

7. Download the cheat sheet from `/download` (only available when logged in)

## Authentication Features

### Registration Process
- Checks for existing email addresses
- Hashes passwords using PBKDF2 with SHA-256
- Adds 8-character random salt to password
- Stores user information in SQLite database
- Automatically logs in user after successful registration
- Redirects existing users to login page

### Login Security
- Verifies email exists in database
- Validates password against stored hash
- Uses secure `check_password_hash` function
- Displays helpful error messages for invalid credentials
- Tracks authentication state across sessions
- Prevents unauthorized access to protected routes

### Protected Routes
- Uses `@login_required` decorator
- Automatically redirects unauthenticated users
- Maintains user session state
- Provides access to `current_user` object
- Checks authentication before serving files

## Technical Details

### Database Schema
**User Model** (`users.db`):
- `id`: Integer, Primary Key (auto-increment)
- `email`: String(100), Unique, Required
- `password`: String(100), Required (hashed)
- `name`: String(1000), Required

### Password Hashing
- **Algorithm**: PBKDF2-HMAC-SHA256
- **Salt Length**: 8 characters
- **Method**: `generate_password_hash()` from Werkzeug
- **Verification**: `check_password_hash()` for authentication
- Never stores plain text passwords

### Session Management
- **Library**: Flask-Login
- **User Loader**: Retrieves user by ID from database
- **Session Cookie**: Tracks authenticated users
- **Current User**: `current_user` proxy available in templates and routes

### File Delivery System
- Serves files from `static/files/` directory
- Uses `send_from_directory()` for secure file serving
- Requires authentication via `@login_required`
- Prevents unauthorized access to resources
- Can enable download mode with `as_attachment=True`

## File Structure

```
Day 68 (Flask Auth)/
├── main.py                 # Flask application with all routes and logic
├── users.db               # SQLite database (auto-created)
├── templates/
│   ├── base.html          # Base template with common elements
│   ├── index.html         # Home page
│   ├── register.html      # Registration form
│   ├── login.html         # Login form
│   └── secrets.html       # Protected user page
├── static/
│   ├── css/              # Stylesheets
│   └── files/
│       └── cheat_sheet.pdf  # Downloadable resource
```

## Learning Concepts

### Flask Fundamentals
- Flask application setup and configuration
- Route creation with multiple HTTP methods (GET, POST)
- Template rendering with Jinja2
- Flash message system for user feedback
- URL generation with `url_for()`
- Redirect functionality after form submission

### Database Operations
- SQLAlchemy ORM with Flask integration
- DeclarativeBase for modern SQLAlchemy 2.0 syntax
- Typed mappings with `Mapped[]` type hints
- Database initialization with `db.create_all()`
- Query execution with `db.session.execute()`
- User existence checking before registration

### Authentication & Security
- Flask-Login extension for session management
- UserMixin for user model integration
- Login manager configuration
- User loader callback function
- Password hashing with Werkzeug security
- Login required decorator for protection
- Session state management
- Secure credential validation

### Form Handling
- POST request processing
- Form data extraction with `request.form`
- Duplicate email detection
- Error handling and user feedback
- Automatic user login after registration
- Conditional redirects based on validation

## Security Notes

### Best Practices Implemented
- **Password Hashing**: Uses industry-standard PBKDF2 with SHA-256
- **Salt Generation**: Random 8-character salt for each password
- **No Plain Text**: Passwords never stored in readable format
- **Session Security**: Flask-Login manages secure sessions
- **Protected Routes**: Decorator-based access control
- **Database Security**: SQLAlchemy ORM prevents SQL injection

### Production Recommendations
- Move SECRET_KEY to environment variables
- Use stronger, randomly generated secret key
- Enable HTTPS for encrypted data transmission
- Implement rate limiting for login attempts
- Add CSRF protection with Flask-WTF
- Consider password strength requirements
- Implement account lockout after failed attempts
- Add email verification for new registrations
- Use secure session cookie settings

## Requirements

- Python 3.x
- Flask (web framework)
- Flask-Login (session management)
- Flask-SQLAlchemy (database ORM)
- Werkzeug (password hashing utilities)

## Environment Setup

### Windows (PowerShell):
```bash
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install flask flask-login flask-sqlalchemy werkzeug
python main.py
```

### macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install flask flask-login flask-sqlalchemy werkzeug
python main.py
```

## How the Code Works

1. **App Initialization**: Creates Flask app with secret key and database configuration
2. **Database Setup**: Defines User model with SQLAlchemy and creates tables
3. **Login Manager**: Configures Flask-Login with user loader function
4. **Home Route**: Renders landing page with authentication state
5. **Registration**: Validates email, hashes password, creates user, logs in automatically
6. **Login**: Checks credentials, verifies password hash, creates session
7. **Protected Pages**: Requires authentication, displays user-specific content
8. **File Download**: Serves protected files only to authenticated users
9. **Logout**: Clears session and redirects to home page

## Next Steps/Improvements

- Add password reset functionality via email
- Implement "Remember Me" checkbox for persistent sessions
- Add user profile page with edit capabilities
- Enable email verification for new accounts
- Implement password strength meter
- Add two-factor authentication (2FA)
- Create admin panel for user management
- Add user profile pictures
- Implement password change functionality
- Add account deletion feature
- Create user activity logs
- Implement OAuth login (Google, GitHub, etc.)

Perfect for learning Flask authentication, password security, session management, and building secure web applications!
