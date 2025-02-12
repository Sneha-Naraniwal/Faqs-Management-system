<p align="center">
  <h2>Frequently Asked Questions (FAQs) with Multi-Language Support</h2>
</p>
This FAQ Management Systemis built with Django and provides seamless multilingual support. It allows users to manage and retrieve FAQs in multiple languages, including English, Hindi, and Bengali.  

---

### Features  
- **Multilingual Support**: Manage FAQs in English, Hindi, and Bengali.  
- **WYSIWYG Editor Integration**: Utilize **django-ckeditor5** for rich text formatting in FAQ answers.  
- **REST API**: Retrieve FAQs in different languages using the `?lang=` query parameter.  
- **Caching**: Enhance performance using **Django's default cache backend**.  
- **Admin Panel**: A user-friendly interface for managing FAQs efficiently.

---

### Deploy Link

### Retrieve FAQs in different languages:
 
**English (Default)**
```
http://65.0.179.163:8000/api/faqs/
```

**Hindi**
```
http://65.0.179.163:8000/api/faqs/{id}/?lang=hi
```

**Bengali**
```
http://65.0.179.163:8000/api/faqs/{id}/?lang=bn
```

### Example ID Usage

**Fetch FAQ in Hindi (hi)**
```
http://65.0.179.163:8000/api/faqs/1/?lang=hi  # Fetch question & answer for ID 1 in Hindi

```

**Fetch FAQ in Bengali (bn)**
```
http://65.0.179.163:8000/api/faqs/2/?lang=bn  # Fetch question & answer for ID 2 in Bengali
```

### Example Response
```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 1,
    "question": "हैलो, मैं एक परियोजना बनाने की कोशिश कर रहा हूं",
    "answer": "मुझे लगता है कि यह काम करता है"
}
```

### Admin Panel  

**Access the Admin Panel:**
```
http://65.0.179.163:8000/admin/
```

**Login Credentials:**
```
echo "Username: admin"
echo "Password: password"
```

**Deployment Details**
```
echo "The FAQ API has been deployed on AWS. Update credentials after login."
```
---

### Demo - Video (YouTube)
[Watch the video on YouTube](https://youtu.be/MA64JPtS4d0?si=w3zVmWrD8mCJ52i2)
---

### Getting Started
To get started with this project, you will need to have the following installed on your local machine:
- **Python 3.12**
- **Git**
- **Redis Server** (for Caching)
  
---

## CKEditor 5 Integration

The project uses **CKEditor 5** for rich text formatting in FAQ answers.

### Steps to Set Up CKEditor 5:
1. **Install the required dependencies for CKEditor 5**.
    ```bash
    pip install django-ckeditor-5
    ```

2. **Add ckeditor` to your `INSTALLED_APPS` in `settings.py**:
    ```python
    INSTALLED_APPS = [
        ...
        'django_ckeditor_5',
        ...
    ]
    ```

--- 

## Backend setup on local machine
### Steps to Set Up
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/QaShah07/BackendBharatFD.git
    ```
2. **Navigate to the Project Folder**:
    ```bash
    cd BackendBharatFD
    ```

3. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    ```

4. **Activate the Virtual Environment**:
    - **On Windows**:
      ```bash
      venv\Scripts\activate
      ```
    - **On macOS/Linux**:
      ```bash
      source venv/bin/activate
      ```

5. **Install Dependencies**:
    ```bash
    pipenv requirements --dev > requirements.txt
    ```


6. **Run Migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7. **Create a Superuser**:
    ```bash
    python manage.py createsuperuser
    ```
8. **change the settings.py**
```
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://host.docker.internal:6379/1',  # to run on docker
        # 'LOCATION': 'redis://127.0.0.1:6379/1' ,   # to run host machine
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
    }
}
```
9. **Start the Server**:
    ```bash
    python manage.py runserver
    ```

10. **Access the Application**:  
    Open your browser and go to:  
    [http://127.0.0.1:8000](http://127.0.0.1:8000)

---


   
## Use Docker to Set Up the Project

---
### **Setup Instructions**
1. **Clone the repository**  
   ```sh
   git clone <your-github-repo-url>
   cd <your-project-folder>
   ```
2. **change the settings.py**
```
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://host.docker.internal:6379/1',  # to run on docker
        # 'LOCATION': 'redis://127.0.0.1:6379/1' ,   # to run host machine
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
    }
}
```
3. **Build Docker images**  
   ```sh
   docker-compose build
   ```

4. **Start the containers**  
   ```sh
   docker-compose up 
   ```

5. **Verify running containers**  
   ```sh
   docker ps
   ```

## API Usage

You can retrieve FAQs in different languages using the following API endpoints:

- **English (Default)**:  
  ```bash
  curl http://127.0.0.1:8000/api/faqs/
  ```

- **Hindi**:  
  ```bash
  curl http://127.0.0.1:8000/api/faqs/{id}/?lang=hi
  ```

- **Bengali**:  
  ```bash
  curl http://127.0.0.1:8000/api/faqs/{id}/?lang=bn

  ```
  ### Example Response:
```json
[{
  "question": "What is Django?",
  "answer": "<p>Django is a web framework for Python.</p>"
}]
```

---

## Admin Panel  
You can manage FAQs through the Django admin panel.  
Access via: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)  
Login with your superuser credentials.

---

## Contribution

1. **Fork the Repository**
2. **Clone your fork**
3. **Create a new branch for your changes**
4. **Make changes and test**
5. **Commit your changes**
6. **Push to your branch**
7. **Open a pull request**

