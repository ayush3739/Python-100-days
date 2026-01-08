# Portfolio Website

A modern, responsive portfolio website built with Flask, featuring a clean design with Font Awesome icons and a mobile-friendly interface.

## 🌟 Features

- **Responsive Design**: Fully responsive layout that works on desktop, tablet, and mobile devices
- **Modern UI/UX**: Clean, professional design with smooth animations and transitions
- **Template Inheritance**: DRY principle with base.html template for consistent header/footer
- **Font Awesome Icons**: Beautiful icons for GitHub, LinkedIn, and other social media
- **Mobile Menu**: Collapsible navigation menu for mobile devices
- **Contact Form**: Functional contact form with Flask backend support
- **Project Showcase**: Grid layout for displaying your projects
- **Easy Customization**: All customizable sections marked with "CHANGE:" comments

## 📁 Project Structure

```
Day 83 (Portfolio Website)/
├── static/
│   └── style.css          # Enhanced CSS with responsive design
├── templates/
│   ├── base.html          # Base template with header & footer
│   ├── home.html          # Homepage with hero section
│   ├── about.html         # About page with skills & experience
│   ├── projects.html      # Projects showcase page
│   └── contact.html       # Contact form page
├── main.py                # Flask application with routes
└── README.md              # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Flask

### Installation

1. Navigate to the project directory:
   ```bash
   cd "Day 83 (Portfolio Website)"
   ```

2. Install Flask (if not already installed):
   ```bash
   pip install flask
   ```

3. Run the application:
   ```bash
   python main.py
   ```

4. Open your browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

## ✏️ Customization Guide

All files contain comments starting with `<!-- CHANGE: -->` or `# CHANGE:` indicating what needs to be customized:

### 1. Personal Information

**In all HTML files**, update:
- Your name (search for "Ayush Maurya")
- Your tagline/role
- Your bio and description

### 2. Social Media Links

**In `templates/base.html`** (footer section):
```html
<a href="https://github.com/yourusername" target="_blank">  <!-- CHANGE: Add your GitHub URL -->
<a href="https://linkedin.com/in/yourprofile" target="_blank">  <!-- CHANGE: Add your LinkedIn URL -->
```

### 3. Contact Information

**In `templates/contact.html`**:
- Email address
- LinkedIn profile
- GitHub username
- Other social media links

### 4. Projects

**In `templates/projects.html` and `templates/home.html`**:
- Project names
- Project descriptions
- Technology tags
- Demo and GitHub links
- Project icons (use Font Awesome icons or add images)

### 5. Skills

**In `templates/about.html`** and **`templates/home.html`**:
- Add your actual technical skills
- Customize skill tags with relevant technologies

### 6. Colors & Branding

**In `static/style.css`** (at the top):
```css
:root {
    --primary-color: #2c3e50;      /* CHANGE: Main color */
    --secondary-color: #3498db;    /* CHANGE: Accent color */
    --accent-color: #e74c3c;       /* CHANGE: Highlight color */
}
```

### 7. Profile Photo

Replace the placeholder in `templates/about.html`:
```html
<!-- Uncomment and add your photo -->
<img src="{{ url_for('static', filename='images/profile.jpg') }}" alt="Your Name">
```

Create a `static/images/` folder and add your profile photo.

### 8. Project Images

Add project screenshots to `static/images/` and update the project cards:
```html
<div class="project-image">
    <img src="{{ url_for('static', filename='images/project1.jpg') }}" alt="Project Name">
</div>
```

## 🎨 Features Breakdown

### Base Template (`base.html`)
- Navigation bar with active page highlighting
- Mobile-responsive hamburger menu
- Footer with social media links
- Integrated Font Awesome for icons

### Home Page (`home.html`)
- Hero section with call-to-action buttons
- Featured projects showcase
- Skills overview section

### About Page (`about.html`)
- Personal introduction
- Skills and technologies
- Education and experience sections
- "Why work with me" highlights

### Projects Page (`projects.html`)
- Comprehensive project grid
- 12 pre-configured project cards
- Hover effects and animations
- Links to demos and GitHub repos

### Contact Page (`contact.html`)
- Contact information cards
- Functional contact form
- Social media links
- Flash message support

## 🔧 Backend Customization

### Contact Form Handler

In `main.py`, customize the contact form handler:

```python
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Add your email sending logic here
        # Example: send_email(name, email, subject, message)
        pass
```

### Adding More Routes

Add new routes in `main.py`:

```python
@app.route('/blog')
def blog():
    return render_template('blog.html')
```

## 📱 Responsive Breakpoints

- **Desktop**: > 992px
- **Tablet**: 768px - 992px
- **Mobile**: < 768px
- **Small Mobile**: < 480px

## 🎭 Font Awesome Icons

The template uses Font Awesome 6.4.0 CDN. Available icon classes:
- `fab fa-github` - GitHub
- `fab fa-linkedin` - LinkedIn
- `fab fa-twitter` - Twitter
- `fas fa-envelope` - Email
- `fab fa-instagram` - Instagram
- And many more at [fontawesome.com](https://fontawesome.com/icons)

## 🌐 Deployment

### Heroku
```bash
# Add Procfile
echo "web: python main.py" > Procfile

# Add requirements.txt
pip freeze > requirements.txt

# Deploy
heroku create your-portfolio
git push heroku main
```

### Vercel/Netlify
Configure for Flask deployment following their respective documentation.

## 📝 To-Do

- [ ] Update personal information
- [ ] Add profile photo
- [ ] Update project details and links
- [ ] Add project screenshots
- [ ] Customize colors
- [ ] Add contact form email functionality
- [ ] Test on all devices
- [ ] Deploy to hosting platform

## 🤝 Contributing

Feel free to fork this project and customize it for your own use!

## 📄 License

This project is open source and available for personal use.

---

**Built with ❤️ using Flask and Font Awesome**
