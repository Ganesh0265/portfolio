# Ganesh Portfolio - Django Project

A modern, interactive portfolio website built with Django and Tailwind CSS, featuring a gamified About section, interactive project showcases, and comprehensive content management.

##  Features

- **Modern Design**: Clean, responsive design with dark/light theme toggle
- **Gamified About Page**: Interactive skill trees, XP bars, and achievements
- **Project Showcase**: Interactive project cards with hover effects
- **Blog System**: Full-featured blog with categories and tags
- **Gallery**: Visual portfolio with lightbox and filtering
- **Testimonials**: Client testimonials carousel
- **Admin Interface**: Easy content management through Django admin
- **SEO Optimized**: Meta tags, structured data, and clean URLs

##  Tech Stack

- **Backend**: Django 4.2+
- **Frontend**: Tailwind CSS, Vanilla JavaScript
- **Database**: SQLite (development), PostgreSQL (production)
- **Rich Text**: CKEditor for content editing
- **Tags**: django-taggit for tagging system
- **Images**: Pillow for image processing

##  Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd portfolio_project
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment setup**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

5. **Database setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

8. **Run development server**
   ```bash
   python manage.py runserver
   ```

##  Initial Setup

1. **Access Admin Panel**
   - Go to `http://localhost:8000/admin/`
   - Login with your superuser credentials

2. **Configure Site Settings**
   - Add your personal information in Site Settings
   - Upload your profile images

3. **Add Content**
   - Create skills with XP levels
   - Add your projects with images
   - Write blog posts
   - Upload gallery items
   - Add testimonials

4. **Social Links**
   - Configure your social media links
   - Set up contact information

##  Project Structure

```
portfolio_project/
├── main/                   # Main Django app
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── admin.py           # Admin configuration
│   └── urls.py            # URL patterns
├── templates/             # HTML templates
│   ├── base.html          # Base template
│   ├── main/              # App templates
│   └── includes/          # Reusable components
├── static/                # Static files
├── media/                 # User uploads
├── requirements.txt       # Python dependencies
└── manage.py             # Django management script
```

##  Customization

### Theme Colors
Edit the Tailwind configuration in `base.html` to customize colors:
```javascript
tailwind.config = {
    theme: {
        extend: {
            colors: {
                primary: '#your-color',
                secondary: '#your-color'
            }
        }
    }
}
```

### Adding New Sections
1. Create new models in `main/models.py`
2. Add admin configuration in `main/admin.py`
3. Create templates in `templates/main/`
4. Add URL patterns in `main/urls.py`
5. Update navigation in `includes/navbar.html`

##  Deployment

### Heroku Deployment
1. Install Heroku CLI
2. Create Heroku app: `heroku create your-app-name`
3. Set environment variables: `heroku config:set SECRET_KEY=your-secret-key`
4. Deploy: `git push heroku main`

### Render Deployment
1. Create a new Web Service on Render
2. Add Build & Start Commands
3. Configure environment variables
4. Set up Static Files
5. Automatic HTTPS & SSL

##  Admin Features

- **Dashboard**: Overview of all content
- **Skills Management**: Add/edit skills with XP levels
- **Project Portfolio**: Manage project showcases
- **Blog System**: Write and publish blog posts
- **Gallery Management**: Upload and organize images
- **Testimonials**: Manage client testimonials
- **Site Settings**: Configure global site settings

##  Development

### Adding New Features
1. Create models for new content types
2. Register models in admin
3. Create views and templates
4. Add URL patterns
5. Update navigation

### Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Static Files
```bash
python manage.py collectstatic
```

##  Content Management

### Skills & Achievements
- Add programming languages and tools
- Set skill levels (0-100)
- Configure XP points for gamification
- Create achievement badges

### Projects
- Upload project images and demos
- Add GitHub and live demo links
- Tag projects with technologies
- Set featured projects for homepage

### Blog Posts
- Write rich-text content with CKEditor
- Organize posts by categories
- Add tags for better organization
- Set featured posts

### Gallery
- Upload project screenshots
- Organize by categories
- Add descriptions and tags
- Enable lightbox viewing

##  Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit pull request

##  Support

For support and questions:
- Create an issue on GitHub
- Email: ganeshpariyar265@gmail.com
- Documentation: Check the code comments and Django docs
