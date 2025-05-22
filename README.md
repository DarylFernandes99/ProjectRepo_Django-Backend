# ProjectRepo Django Backend

A comprehensive Django REST API backend that powers multiple AI/ML-based web applications including image colorization, low-light image enhancement, and poem generation.

## 🚀 Overview

This repository serves as the backend for the ProjectRepo website, providing REST API endpoints for three distinct machine learning applications:

- **Image Colorization**: Transform black and white images into colorized versions using deep learning
- **Low-Light Image Enhancement (LLIE)**: Enhance dark/low-light images using Generative Adversarial Networks (GANs)
- **Phrase-based Poem Generation**: Generate creative poems based on input phrases using natural language processing

## 🏗️ Architecture

The project follows Django's modular architecture with separate apps for each functionality:

```
ProjectRepo_Django-Backend/
├── keras_models/          # Main Django project configuration
│   ├── settings.py        # Project settings and configuration
│   ├── urls.py           # Main URL routing
│   ├── wsgi.py           # WSGI configuration for deployment
│   └── asgi.py           # ASGI configuration for async support
├── colorize/             # Image colorization app
│   ├── models.py         # Colorize data models and ML processing
│   ├── api/              # REST API implementation
│   │   ├── views.py      # API views and endpoints
│   │   ├── serializers.py # Data serialization
│   │   └── urls.py       # App-specific URL routing
│   └── migrations/       # Database migrations
├── llie/                 # Low-light image enhancement app
│   ├── models.py         # LLIE data models and GAN processing
│   ├── api/              # REST API implementation
│   └── migrations/       # Database migrations
├── poem/                 # Poem generation app
│   ├── models.py         # Poem data models and NLP processing
│   ├── api/              # REST API implementation
│   ├── Trained Model/    # Contains tokenizer.pkl for text processing
│   └── migrations/       # Database migrations
├── feedback/             # User feedback and email system
│   ├── models.py         # Feedback data models and email handling
│   ├── api/              # REST API implementation
│   └── migrations/       # Database migrations
├── requirements.txt      # Python dependencies
├── manage.py            # Django management script
├── Procfile             # Heroku deployment configuration
├── runtime.txt          # Python version specification
└── urls.py              # Global API URL routing
```

## 🛠️ Technology Stack

### Backend Framework
- **Django 3.1.12**: Web framework
- **Django REST Framework 3.12.2**: API development
- **Django CORS Headers**: Cross-origin resource sharing

### Machine Learning & AI
- **TensorFlow 2.4.2**: Deep learning framework
- **Keras 2.4.3**: High-level neural network API
- **TensorFlow Addons 0.12.1**: Additional TensorFlow functionality
- **OpenCV 4.5.1.48**: Computer vision and image processing
- **NumPy 1.19.5**: Numerical computing
- **Pillow 8.2.0**: Image processing library

### Database & Storage
- **SQLite**: Default database (development)
- **PostgreSQL support**: Via psycopg2 (production ready)

### Deployment & Infrastructure
- **Gunicorn 20.1.0**: WSGI HTTP server
- **WhiteNoise 5.2.0**: Static file serving
- **Heroku**: Cloud platform deployment

## 📋 Prerequisites

- Python 3.7.9 (specified in runtime.txt)
- pip (Python package manager)
- Virtual environment (recommended)
- Git for version control

## 🔧 Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd ProjectRepo_Django-Backend
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configuration Setup

#### Secret Key Configuration
Create and configure the Django secret key:

```bash
# Navigate to the keras_models directory
cd keras_models

# Create randomKey.txt file and add your Django secret key
echo "your-secret-key-here" > randomKey.txt
```

#### Email Configuration (Optional)
If you want to enable email functionality for the feedback system, update the email settings in `keras_models/settings.py`:

```python
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
```

#### Model Links Configuration
Update the model URLs in each app's `models.py` file:

- `colorize/models.py`: Add your colorization model URL
- `llie/models.py`: Add your LLIE model URL  
- `poem/models.py`: Add your poem generation model URL

```python
# Example in models.py files
file_model = 'https://your-model-hosting-url.com/model.h5'
```

### 5. Database Setup

```bash
# Create and apply migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser account
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`

## 🔌 API Endpoints

The API provides RESTful endpoints for each application module:

### Base URL
```
http://127.0.0.1:8000/api/
```

### Image Colorization
```
GET    /api/colorize/          # List all colorization requests
POST   /api/colorize/          # Submit image for colorization
GET    /api/colorize/{id}/     # Get specific colorization result
DELETE /api/colorize/{id}/     # Delete colorization request
```

**Request Format:**
```json
{
  "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhE..."
}
```

**Response Format:**
```json
{
  "id": 1,
  "image": "/media/images/image.png",
  "predicted": true,
  "result": "http://127.0.0.1:8000/media/images/image_pred.png"
}
```

### Low-Light Image Enhancement (LLIE)
```
GET    /api/low-light/         # List all LLIE requests
POST   /api/low-light/         # Submit image for enhancement
GET    /api/low-light/{id}/    # Get specific enhancement result
DELETE /api/low-light/{id}/    # Delete enhancement request
```

**Request/Response Format:** Similar to colorization endpoints

### Poem Generation
```
GET    /api/poem/              # List all poem generation requests
POST   /api/poem/              # Generate poem from phrase
GET    /api/poem/{id}/         # Get specific poem result
DELETE /api/poem/{id}/         # Delete poem request
```

**Request Format:**
```json
{
  "phrase": "A beautiful sunset",
  "length": 50
}
```

**Response Format:**
```json
{
  "id": 1,
  "phrase": "A beautiful sunset",
  "length": 50,
  "result": "A beautiful sunset glows...\n[Generated poem content]"
}
```

### Feedback System
```
GET    /api/feedback/          # List all feedback (admin only)
POST   /api/feedback/          # Submit feedback
GET    /api/feedback/{id}/     # Get specific feedback
DELETE /api/feedback/{id}/     # Delete feedback
```

**Request Format:**
```json
{
  "email": "user@example.com",  // Optional
  "subject": "Feedback Subject",
  "message": "Detailed feedback message"
}
```

## 🤖 Machine Learning Models

### Image Colorization Model
- **Architecture**: Convolutional Neural Network
- **Input**: Grayscale images (256x256)
- **Output**: RGB colorized images
- **Framework**: TensorFlow/Keras

### Low-Light Image Enhancement Model
- **Architecture**: Generative Adversarial Network (GAN)
- **Input**: Low-light RGB images (256x256)
- **Output**: Enhanced bright images
- **Special Features**: Instance Normalization, median filtering
- **Framework**: TensorFlow/Keras with TensorFlow Addons

### Poem Generation Model
- **Architecture**: Recurrent Neural Network (LSTM/GRU)
- **Input**: Text phrases with specified length
- **Output**: Generated poetry text
- **Preprocessing**: Tokenization using pre-trained tokenizer
- **Framework**: TensorFlow/Keras

## 📁 Data Models

### Colorize Model
```python
class Colorize(models.Model):
    image = models.ImageField(upload_to='images')
    predicted = models.BooleanField(default=False)
    result = models.CharField(max_length=250, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
```

### LLIE Model
```python
class Llie(models.Model):
    image = models.ImageField(upload_to='images')
    predicted = models.BooleanField(default=False)
    result = models.CharField(max_length=250, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
```

### Poem Model
```python
class Poem(models.Model):
    phrase = models.CharField(max_length=250)
    length = models.IntegerField()
    result = models.TextField(blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
```

### Feedback Model
```python
class Feedback(models.Model):
    email = models.EmailField(blank=True)
    subject = models.CharField(max_length=50)
    message = models.TextField()
```

## 🔒 Security Features

- **CORS Configuration**: Properly configured for frontend integration
- **File Upload Limits**: 25MB maximum upload size
- **Base64 Image Handling**: Secure image processing and validation
- **Email Validation**: Built-in email field validation
- **Secret Key Management**: External secret key file
- **HTTPS Ready**: SSL/TLS configuration available for production

## 🚀 Deployment

### Heroku Deployment

The project is configured for Heroku deployment with:

- `Procfile`: Specifies the web process
- `runtime.txt`: Python version specification
- `requirements.txt`: Dependencies list

```bash
# Deploy to Heroku
heroku create your-app-name
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### Production Settings

For production deployment, update the following in `settings.py`:

```python
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com', 'your-heroku-app.herokuapp.com']

# Enable security settings
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_SECONDS = 1
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

## 🧪 Testing

Run the test suite:

```bash
python manage.py test
```

Individual app testing:

```bash
python manage.py test colorize
python manage.py test llie
python manage.py test poem
python manage.py test feedback
```

## 📊 Performance Considerations

- **Model Loading**: Models are loaded from external URLs and cached in memory
- **Image Processing**: Images are automatically resized to optimal dimensions
- **Memory Management**: Old files are automatically cleaned up to save storage
- **Database Optimization**: Automatic cleanup of old prediction records

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Projects

- [ProjectRepo Frontend](https://github.com/DarylFernandes99/ProjectRepo) - React frontend for this backend

## 📈 Roadmap

- [ ] Add model caching for better performance
- [ ] Implement user authentication
- [ ] Add batch processing capabilities
- [ ] Integrate more ML models
- [ ] Add comprehensive monitoring and logging
- [ ] Implement rate limiting
- [ ] Add comprehensive API documentation with Swagger/OpenAPI

---

**Note**: Make sure to add your actual model URLs in the respective `models.py` files and configure email settings before deploying to production.
