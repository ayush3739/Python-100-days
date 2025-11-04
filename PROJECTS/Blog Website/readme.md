# Blog Website with Flask

A full-featured blog website built with Flask that includes a contact form with email functionality, blog post display, and dynamic routing.

## Features
- **Dynamic Blog Posts**: Display blog posts fetched from an external API
- **Contact Form**: Functional contact form with email notification system
- **Email Integration**: Sends form submissions via SMTP email
- **Responsive Design**: Multiple page templates for home, about, contact, and post pages
- **RESTful Routing**: Clean URL structure for blog posts and pages
- **Environment Variables**: Secure credential management using .env file

## Pages
- **Home Page** (`/`): Displays all blog posts in a card layout
- **About Page** (`/about`): Information about the blog
- **Contact Page** (`/contact`): Contact form with POST handling
- **Individual Post** (`/post/<id>`): Dynamic post display by ID

## How to Use
1. Install required dependencies:
   ```bash
   pip install flask python-dotenv requests
   ```

2. Create a `.env` file with your credentials:
   ```
   email=your_email@gmail.com
   to_email=recipient@email.com
   pass=your_app_password
   ```

3. Run the application:
   ```bash
   python main.py
   ```

4. Navigate to `http://localhost:5000` in your browser

## Contact Form Features
- Captures name, email, phone number, and message
- Validates form submissions (POST method)
- Sends email notifications when form is submitted
- Displays confirmation message after successful submission
- SMTP integration with Gmail (or other email providers)

## Technical Details
- **API Integration**: Fetches blog data from `https://api.npoint.io/a488fedba3cea47fdfa7`
- **Email Protocol**: Uses SMTP with STARTTLS encryption
- **Template Engine**: Jinja2 for dynamic HTML rendering
- **Form Handling**: Supports both GET and POST methods

## Files Structure
- `main.py` - Flask application with routes and email functionality
- `templates/` - HTML templates for all pages
  - `index.html` - Home page with blog post listings
  - `about.html` - About page
  - `contact.html` - Contact form page
  - `post.html` - Individual blog post display
  - `header.html` - Header component
  - `footer.html` - Footer component
- `static/` - CSS, JavaScript, and image assets
- `.env` - Environment variables (not included, create your own)

## Learning Concepts
- Flask web framework fundamentals
- RESTful API integration
- Form handling and validation
- SMTP email sending
- Environment variable management
- Template inheritance and rendering
- Dynamic routing with URL parameters
- HTTP methods (GET/POST)

## Security Notes
- Uses environment variables for sensitive credentials
- SMTP authentication with app-specific passwords
- Email addresses hidden from source code
- STARTTLS for secure email transmission

## Requirements
- Python 3.x
- Flask
- python-dotenv
- requests
- smtplib (included with Python)

## Email Setup
For Gmail, you need to:
1. Enable 2-factor authentication
2. Generate an app-specific password
3. Use the app password in your .env file

Perfect for learning Flask basics, API integration, and building a functional blog with contact capabilities!
