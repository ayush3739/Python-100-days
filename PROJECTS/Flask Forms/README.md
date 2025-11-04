# Flask Forms Application

A simple Flask web application demonstrating basic form handling with POST method for user login credentials.

## Features
- **HTML Form Rendering**: Display login form with username and password fields
- **POST Request Handling**: Process form submissions using Flask's request object
- **Form Data Extraction**: Retrieve and display submitted form data
- **Clean Route Structure**: Separate routes for form display and data processing

## Routes
- **Home Page** (`/`): Displays the login form
- **Login Handler** (`/login`): Processes POST requests and displays submitted data

## How to Use
1. Install Flask:
   ```bash
   pip install flask
   ```

2. Run the application:
   ```bash
   python main.py
   ```

3. Navigate to `http://localhost:5000` in your browser

4. Fill in the username and password fields

5. Submit the form to see the processed data

## Form Structure
The login form includes:
- **Username Field**: Text input for username
- **Password Field**: Password input (hidden characters)
- **Submit Button**: Triggers POST request to `/login` route

## Technical Details
- **HTTP Method**: POST for secure form submission
- **Form Handling**: Uses Flask's `request.form` dictionary
- **Response Format**: HTML with form data displayed
- **Debug Mode**: Enabled for development with auto-reload

## Files
- `main.py` - Flask application with form handling logic
- `templates/forms.html` - HTML form template

## Code Highlights
```python
@app.route('/login', methods=["POST"])
def receive_data():
    name = request.form['username']
    password = request.form['password']
    return f"<h1>Name: {name} Password: {password}</h1>"
```

## Learning Concepts
- Flask application setup and configuration
- HTML form creation and rendering
- POST request handling in Flask
- Form data extraction with request.form
- Route methods specification
- Basic Flask templating with render_template

## Security Considerations
**Note**: This is a learning project and demonstrates basic concepts. In a production application:
- Never display passwords in plain text
- Use password hashing (bcrypt, argon2)
- Implement CSRF protection
- Use HTTPS for secure transmission
- Validate and sanitize user input
- Use session management for authentication

## Requirements
- Python 3.x
- Flask 2.3.2 or higher

## Next Steps for Enhancement
- Add form validation
- Implement password hashing
- Create user database
- Add session management
- Implement CSRF protection
- Style the form with CSS
- Add error handling

Perfect for understanding the fundamentals of form handling in Flask applications!
