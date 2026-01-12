# Blog Website with Flask

A full-featured blogging platform built with Flask featuring user authentication, admin controls, rich text editing with CKEditor, commenting system with Gravatar avatars, Bootstrap 5 styling, and SMTP email integration for contact messages.

## Features

- **User Authentication**: Complete registration and login system with password hashing
- **Admin Controls**: Admin-only access for creating, editing, and deleting posts
- **Rich Text Editor**: CKEditor integration for creating formatted blog posts
- **Comment System**: Authenticated users can comment on posts with timestamps
- **Gravatar Avatars**: Automatic avatar generation for commenters
- **Bootstrap 5**: Responsive, modern design that works on all devices
- **Email Contact**: SMTP-powered contact form with Gmail integration
- **Database Relationships**: Proper foreign key relationships between users, posts, and comments
- **Flash Messages**: User feedback for authentication and form submissions
- **Admin Dashboard**: Special privileges for post management

## Pages/Routes

- **Home** (`/`): Display all blog posts in a clean layout
- **Register** (`/register`): Create new user account with validation
- **Login** (`/login`): Authenticate existing users
- **Logout** (`/logout`): End user session
- **Post View** (`/post/<id>`): View individual post with comments (comment form for logged-in users)
- **New Post** (`/new-post`): Create new blog post (admin only)
- **Edit Post** (`/edit-post/<id>`): Modify existing post (admin only)
- **Delete Post** (`/delete/<id>`): Remove post from database (admin only)
- **About** (`/about`): About page information
- **Contact** (`/contact`): Contact form with email sending (requires login)
- **Debug User** (`/debug/user/<id>`): JSON view of user data (admin only)

## How to Use

1. Install required dependencies:
   ```bash
   pip install flask flask-bootstrap flask-ckeditor flask-gravatar flask-login flask-sqlalchemy python-dotenv
   ```

2. Create a `.env` file in the project directory:
   ```
   secret_key=your-super-secret-key-here
   email=your-gmail@example.com
   pass=your-gmail-app-password
   to_email=recipient@example.com
   ```

3. Run the application:
   ```bash
   python main.py
   ```

4. Navigate to `http://127.0.0.1:5000` in your browser

5. Register a new account (first user or manually set `is_admin=True` in database)

6. As admin: Create, edit, and delete blog posts

7. As regular user: Browse posts and add comments

8. Use contact form to send email messages

## Admin Features

### Creating Admin Users
- New users are created with `is_admin=False` by default
- Manually update database to set `is_admin=True` for admin access
- Admin users can create, edit, and delete posts
- Only admins see post management buttons

### Admin-Only Routes
- **Create Post**: Rich text editor for new blog posts
- **Edit Post**: Modify existing post content and metadata
- **Delete Post**: Remove posts from database
- **Debug Endpoints**: View user data in JSON format

### Admin Decorator
- Custom `@admin_only` decorator protects admin routes
- Returns 403 Forbidden for non-admin users
- Checks both authentication and admin status

## Comment System Features

- **Authentication Required**: Must be logged in to comment
- **Character Limit**: Comments limited to 300 characters
- **Timestamps**: Automatic UTC timestamp for each comment
- **Gravatar Integration**: Shows user avatar based on email
- **Nested Display**: Comments displayed below posts
- **Author Information**: Shows commenter name and profile picture

## Technical Details

### Database Models

**User Model** (`users` table):
- `id`: Primary Key
- `email`: Unique, required
- `password`: Hashed password
- `name`: User display name
- `is_admin`: Boolean flag for admin access
- Relationships: `posts`, `comments`

**BlogPost Model** (`blog_posts` table):
- `id`: Primary Key
- `author_id`: Foreign Key to User
- `title`: Unique post title
- `subtitle`: Post subtitle
- `date`: Publication date (string format)
- `body`: Post content (Text field)
- `img_url`: Featured image URL
- Relationships: `author`, `comments`

**Comments Model** (`comments` table):
- `id`: Primary Key
- `author_id`: Foreign Key to User
- `post_id`: Foreign Key to BlogPost
- `text`: Comment content (max 300 chars)
- `created_at`: UTC timestamp
- Relationships: `comment_author`, `parent_post`

### Email Integration
- **SMTP Server**: Gmail (smtp.gmail.com:587)
- **Security**: STARTTLS encryption
- **Authentication**: App-specific password required
- **Error Handling**: Returns success/failure status
- **Message Format**: EmailMessage with proper headers

### Form Classes (forms.py)

- **CreatePostForm**: Title, subtitle, image URL, CKEditor body
- **RegisterForm**: Name, email, password with validation
- **LoginForm**: Email and password fields
- **CommentForm**: CKEditor field for comment text

### Security Features
- **Password Hashing**: PBKDF2-SHA256 with 8-char salt
- **Flask-Login**: Session management and user tracking
- **CSRF Protection**: Available through Flask-WTF
- **Environment Variables**: Credentials stored in .env file
- **Admin Authorization**: Decorator-based access control
- **SQL Injection Protection**: SQLAlchemy ORM prevents injection

## File Structure

```
Day 69 (Blog Website)/
├── main.py                 # Flask application with all routes
├── forms.py               # WTForms form definitions
├── posts.db              # SQLite database (auto-created)
├── .env                  # Environment variables (create this)
├── templates/
│   ├── header.html       # Navigation header component
│   ├── footer.html       # Footer component
│   ├── index.html        # Home page with post listings
│   ├── post.html         # Individual post view with comments
│   ├── make-post.html    # Create/edit post form
│   ├── register.html     # Registration form
│   ├── login.html        # Login form
│   ├── about.html        # About page
│   └── contact.html      # Contact form
├── static/
│   ├── css/             # Stylesheets
│   ├── js/              # JavaScript files
│   └── images/          # Image assets
```

## Learning Concepts

### Flask Advanced Features
- Custom decorator creation (`@admin_only`)
- Multiple database relationships
- Template inheritance and components
- Flash message categories and styling
- File upload handling (for images)
- Form validation with WTForms

### Database Relationships
- One-to-many: User → BlogPosts
- One-to-many: User → Comments
- One-to-many: BlogPost → Comments
- Foreign key constraints
- Relationship back_populates

### Authentication & Authorization
- Registration with duplicate email checking
- Login with password verification
- Admin role-based access control
- Session persistence with Flask-Login
- Protected routes with decorators

### Rich Text Editing
- CKEditor integration with Flask
- CKEditorField in WTForms
- HTML content storage and display
- Safe HTML rendering in templates

### Email Functionality
- SMTP connection setup
- EmailMessage construction
- TLS encryption
- App password authentication
- Error handling and user feedback

## Security Notes

### Best Practices Implemented
- **Environment Variables**: Credentials not in source code
- **Password Hashing**: PBKDF2 with salt
- **Session Management**: Secure cookie-based sessions
- **Admin Authorization**: Role-based access control
- **ORM Usage**: Protection against SQL injection
- **TLS Email**: Encrypted email transmission

### Production Recommendations
- Use stronger SECRET_KEY (random, long)
- Enable HTTPS for all communications
- Implement CSRF protection with Flask-WTF
- Add rate limiting for login attempts
- Implement password reset functionality
- Add email verification for new accounts
- Use production WSGI server (Gunicorn, uWSGI)
- Set secure session cookie flags
- Implement logging for security events

## Requirements

- Python 3.x
- Flask (web framework)
- Flask-Bootstrap (Bootstrap 5 integration)
- Flask-CKEditor (rich text editing)
- Flask-Gravatar (avatar generation)
- Flask-Login (session management)
- Flask-SQLAlchemy (database ORM)
- python-dotenv (environment variables)

## Gmail Setup for Contact Form

1. Enable 2-Factor Authentication on your Gmail account
2. Go to Google Account Settings → Security
3. Generate an App Password (select "Mail" and your device)
4. Use the generated 16-character password in your `.env` file
5. Regular Gmail password will NOT work for SMTP

## Environment Setup

### Windows (PowerShell):
```bash
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install flask flask-bootstrap flask-ckeditor flask-gravatar flask-login flask-sqlalchemy python-dotenv
python main.py
```

### macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install flask flask-bootstrap flask-ckeditor flask-gravatar flask-login flask-sqlalchemy python-dotenv
python main.py
```

## How the Code Works

1. **Initialization**: Sets up Flask app with extensions and loads environment variables
2. **Database**: Creates tables for users, posts, and comments with relationships
3. **Authentication**: Handles registration, login, and session management
4. **Authorization**: Custom decorator checks admin status for protected routes
5. **Post Management**: Admins can create, edit, and delete blog posts with rich text
6. **Comments**: Logged-in users can add comments to posts with validation
7. **Email**: Contact form sends messages via Gmail SMTP with proper error handling
8. **Templates**: Bootstrap 5 provides responsive design with header/footer components

## Next Steps/Improvements

- Add rich text editing for comments
- Implement post categories and tags
- Add search functionality for posts
- Create user profile pages
- Add pagination for post listings
- Implement post drafts and scheduling
- Add social media sharing buttons
- Create RSS feed for blog posts
- Add like/reaction system for posts
- Implement comment replies (nested comments)
- Add image upload for posts
- Create sitemap for SEO
- Add analytics dashboard for admins
- Implement post revision history

Perfect for learning Flask web development, database relationships, authentication/authorization, rich text editing, and building a production-ready blogging platform!
