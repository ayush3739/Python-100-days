# Portfolio Website with Flask

A modern, responsive portfolio website built with Flask featuring multiple pages, a contact form, and clean Bootstrap-inspired design. Perfect for showcasing projects, skills, and professional information.

## Features

- **Multi-Page Structure**: Home, About, Projects, and Contact pages
- **Template Inheritance**: Base template with consistent header and footer
- **Responsive Design**: Mobile-friendly layout that works on all devices
- **Contact Form**: Form submission with POST handling and flash messages
- **Clean Navigation**: Navigation bar with active page highlighting
- **Professional Layout**: Modern design suitable for professional portfolios
- **Easy Customization**: Clearly marked sections for personalization
- **Static Asset Management**: Organized CSS and image structure

## Pages

### Home Page (`/` and `/home`)
- Hero section with introduction
- Call-to-action buttons
- Featured projects preview
- Skills overview
- Links to other sections

### About Page (`/about`)
- Personal introduction and bio
- Professional background
- Skills and technologies
- Education and experience
- Professional photo (optional)
- Career highlights

### Projects Page (`/projects`)
- Project showcase grid
- Project cards with descriptions
- Technology tags
- Links to demos and GitHub
- Categories or filters
- Project images

### Contact Page (`/contact`)
- Contact information display
- Contact form with validation
- Social media links
- Email, LinkedIn, GitHub links
- Form submission with feedback
- Success/error messages

## How to Use

1. Install Flask:
   ```bash
   pip install flask
   ```

2. Run the application:
   ```bash
   python main.py
   ```

3. Navigate to `http://127.0.0.1:5000` in your browser

4. Customize content in templates:
   - Update personal information
   - Add your projects
   - Modify skills and experience
   - Update social media links

5. Customize styling in `static/style.css`

## Contact Form Features

### Form Fields
- **Name**: User's full name
- **Email**: Contact email address
- **Subject**: Message subject line
- **Message**: Detailed message content

### Form Handling
- **GET Request**: Displays empty form
- **POST Request**: Processes form submission
- **Flash Messages**: Shows success confirmation
- **Redirect**: Returns to contact page after submission
- **Validation**: Fields marked as required in HTML

### Current Implementation
```python
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # TODO: Add email sending or database storage
        
        flash('Thank you for your message! I will get back to you soon.')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')
```

## Technical Details

### Flask Application Structure
- **Route Handlers**: Functions for each page
- **Template Rendering**: Jinja2 template engine
- **Static Files**: CSS and images served from `/static`
- **Flash Messages**: Session-based user feedback
- **URL Building**: `url_for()` for dynamic URLs

### Template System
- **Base Template**: `base.html` with common elements
- **Template Inheritance**: Other templates extend base
- **Jinja2 Syntax**: Variables, loops, conditionals
- **URL Generation**: Dynamic link creation
- **Static File Linking**: `url_for('static', filename='...')`

### HTTP Methods
- **GET**: Retrieve and display pages
- **POST**: Submit form data
- **Redirect**: Navigate after form submission

### Session Management
- **Secret Key**: Required for flash messages
- **Session Storage**: Server-side session data
- **Flash Messages**: Temporary user feedback

## File Structure

```
Day 83 (Portfolio Website)/
├── main.py                 # Flask application with routes
├── templates/
│   ├── base.html          # Base template (header, footer)
│   ├── home.html          # Homepage content
│   ├── about.html         # About page content
│   ├── projects.html      # Projects showcase
│   └── contact.html       # Contact form
├── static/
│   ├── style.css         # Custom stylesheets
│   └── images/           # Images and assets (create as needed)
└── README.md             # This file
```

## Customization Guide

### Personal Information
1. Open each template file
2. Search for placeholder text (e.g., "Your Name")
3. Replace with your actual information
4. Update links to your profiles

### Projects Section
1. Edit `projects.html`
2. Add project cards with:
   - Project name
   - Description
   - Technologies used
   - Demo/GitHub links
   - Project screenshots

### Styling
1. Edit `static/style.css`
2. Modify colors, fonts, spacing
3. Add custom animations
4. Adjust responsive breakpoints

### Adding Images
1. Create `static/images/` folder
2. Add your images
3. Reference in templates:
   ```html
   <img src="{{ url_for('static', filename='images/photo.jpg') }}">
   ```

## Learning Concepts

### Flask Basics
- Application initialization
- Route decoration
- Template rendering
- Static file serving
- HTTP method handling
- Flash message system
- URL generation

### Web Development
- HTML template structure
- CSS styling
- Responsive design principles
- Form handling
- User feedback mechanisms
- Navigation systems

### Template Engineering
- Jinja2 template syntax
- Template inheritance
- Variable interpolation
- URL generation in templates
- Conditional rendering
- Loop iteration

### Form Processing
- HTML form creation
- POST data retrieval
- Form validation
- User feedback
- Redirect patterns
- Flash message display

## Requirements

- Python 3.x
- Flask (web framework)

## Environment Setup

### Windows (PowerShell):
```bash
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install flask
python main.py
```

### macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install flask
python main.py
```

## How the Code Works

1. **App Initialization**: Creates Flask app with secret key
2. **Route Definitions**: Maps URLs to handler functions
3. **Template Rendering**: Loads and renders HTML templates
4. **Form Handling**: Processes contact form submissions
5. **Flash Messages**: Provides user feedback
6. **Static Files**: Serves CSS and images
7. **URL Generation**: Creates dynamic links

## Extending the Contact Form

### Add Email Sending (SMTP)
```python
import smtplib
from email.message import EmailMessage

def send_email(name, email, subject, message):
    msg = EmailMessage()
    msg['From'] = 'your-email@gmail.com'
    msg['To'] = 'recipient@example.com'
    msg['Subject'] = subject
    msg.set_content(f"From: {name} ({email})\n\n{message}")
    
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login('your-email@gmail.com', 'app-password')
        smtp.send_message(msg)
```

### Add Database Storage
```python
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    subject = db.Column(db.String(200))
    message = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.utcnow)
```

### Add Form Validation
```python
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Message')
```

## Security Considerations

### Current Implementation
- **Secret Key**: Hardcoded (should be in environment variable)
- **No CSRF Protection**: Consider adding Flask-WTF
- **No Input Validation**: Should validate email format, message length
- **No Rate Limiting**: Vulnerable to spam

### Improvements for Production
- Move secret key to environment variable
- Add CSRF protection with Flask-WTF
- Implement form validation
- Add rate limiting (Flask-Limiter)
- Sanitize user input
- Add reCAPTCHA
- Enable HTTPS
- Implement email verification

## Next Steps/Improvements

- Integrate email sending (SMTP)
- Add database for contact submissions
- Implement form validation with Flask-WTF
- Add CSRF protection
- Create admin dashboard to view messages
- Add blog section with posts
- Implement project filtering/search
- Add dark mode toggle
- Include testimonials section
- Add resume download link
- Create sitemap for SEO
- Add Google Analytics
- Implement contact form reCAPTCHA
- Add social media feed integration
- Create print-friendly resume view

Perfect for learning Flask basics, template rendering, form handling, and building a professional portfolio website to showcase your work!
