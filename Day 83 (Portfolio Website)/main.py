from flask import Flask, render_template, request, url_for, redirect, flash
# BACKEND TODO: Import additional modules as needed (e.g., smtplib for email, database modules, etc.)

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # CHANGE: Add a secure secret key for flash messages


@app.route('/')
@app.route('/home')
def home():
    """Home page route"""
    return render_template('home.html')


@app.route('/about')
def about():
    """About page route"""
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page route - handles both GET and POST requests"""
    if request.method == 'POST':
        # BACKEND TODO: Add form handling logic here
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # BACKEND TODO: Add your email sending logic here
        # Example: send_email(name, email, subject, message)
        # Or save to database: save_contact_form(name, email, subject, message)
        
        # Flash success message
        flash('Thank you for your message! I will get back to you soon.')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')


@app.route('/projects')
def projects():
    """Projects page route"""
    # BACKEND TODO: You can add logic here to fetch projects from a database
    # projects_list = get_all_projects_from_db()
    # return render_template('projects.html', projects=projects_list)
    return render_template('projects.html')


# BACKEND TODO: Add more routes as needed
# Example: Blog posts, project details, admin panel, etc.

if __name__ == '__main__':
    app.run(debug=True)
