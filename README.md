# Quiz Application (Django + Tailwind CSS)

A full-featured Quiz & Events web application built with **Django**, styled using **Tailwind CSS**, and configured with **django-tailwind** for modern, fast UI development.

The project supports:
- User authentication (login, registration, logout)
- Quiz listing, quiz details and quiz results
- Event management (with automatic deletion logic)
- Tailwind CSS integration with automatic live rebuilding
- Browser auto-reload for faster development workflow

---

## 📌 Features

- Django-based backend with Model–View–Template architecture
- Tailwind CSS for styling
- django-browser-reload for auto refresh
- Widget-tweaks for easy form styling
- Clean modular project structure
- Ready for deployment

---

# 🚀 Installation & Setup Guide

Follow these steps to run the project on your local system.

---

## 1. Clone the Repository

```bash
git clone https://github.com/AYUSHIPATEL123/quize_app.git
cd quize_app
```
## 2. Create Virtual Environment
python -m venv .venv

Activate Virtual Environment

Windows:
```bash
.venv\Scripts\activate
```

Mac / Linux:
```bash
source .venv/bin/activate
```
## 3. Install Dependencies

If requirements.txt exists:
```bash
pip install -r requirements.txt
```

Else install manually:
```bash
pip install django django-tailwind django-browser-reload widget-tweaks "django-tailwind[reload]"
```
🎨 Tailwind CSS Setup

The project uses django-tailwind, which creates a separate Django app for Tailwind.

## 4. Initialize Tailwind (if not already created)
```bash
python manage.py tailwind init theme
```
## 5. Configure Django Settings

In settings.py:

INSTALLED_APPS = [
    ...,                             
    "tailwind",                          
    "theme",                              
    "django_browser_reload",                         
    "widget_tweaks",                     
]

TAILWIND_APP_NAME = 'theme'
NPM_BIN_PATH = r'C:\Program Files\nodejs\npm.cmd' (windows) (put you path) [in cmd type  
INTERNAL_IPS = ['127.0.0.1',]

MIDDLEWARE = [
    ...
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

## 6. Install Tailwind Node Dependencies
```bash
python manage.py tailwind install
```

This installs Tailwind, PostCSS, Autoprefixer etc.

## 7. Apply Migrations
```bash
python manage.py migrate
```
## 8. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

🟢 Running the Project (Very Important)
✔ Start Tailwind CSS Watcher (Terminal 1)
```bash
python manage.py tailwind start
```

This listens for HTML changes and rebuilds CSS automatically.

✔ Start Django Development Server (Terminal 2)
```bash
python manage.py runserver
```

Now visit:
👉 http://127.0.0.1:8000/

# 🎨 Tailwind Configuration Notes

Update tailwind.config.js:

module.exports = {              
  content: [           
    "./templates/**/*.html",                   
    "./**/templates/**/*.html",              
  ],          
  theme: {             
    extend: {},               
  },                     
  plugins: [],               
}            


If you use dynamic classes (alerts, messages), add a safelist to prevent purge.

## 🚨 Troubleshooting
Tailwind classes not applying?

✔ Run:
```bash
python manage.py tailwind start
```

✔ Check content[] paths in tailwind.config.js.

Browser does not auto-reload?

Ensure:

"django_browser_reload",                   
"django_browser_reload.middleware.BrowserReloadMiddleware",


are included in settings.

## 📦 Deployment Notes

Before deploying, run:
```bash
python manage.py collectstatic
python manage.py tailwind build
```

## 🤝 Contributing

Feel free to open issues or submit PRs to improve features, UI, or performance.



# Install django-tailwind with reload support
```bash
pip install "django-tailwind[reload]"
```

## ✔ This installs:

django-tailwind

django-browser-reload (for auto refresh)

All required dependencies

## 🔧 Verify installation

Run:
```bash
pip show django-tailwind
pip show django-browser-reload
```

You should see both installed.

 ## 🛠 Add to settings.py
INSTALLED_APPS = [
    ...                                  
    "tailwind",                     
    "theme",                        
    "django_browser_reload",                      
]


Middleware:

MIDDLEWARE = [
    ...           
    "django_browser_reload.middleware.BrowserReloadMiddleware",                  
]


URLs:                 
root urls.py                 
urlpatterns = [
    ...                                 
    path("__reload__/", include("django_browser_reload.urls")),             
]

🚀 Start Tailwind watcher
python manage.py tailwind start


# 📄 License

This project is licensed under the MIT License.
