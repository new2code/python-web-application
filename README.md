# Python Flask Web Application

A beginner-friendly web application built with Python and Flask to demonstrate web development concepts. This app serves a dynamic web page with interactive features and provides a JSON API endpoint for learning full-stack development fundamentals.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/new2code/python-web-application
   cd python-web-application
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   *Note: If you see a warning about upgrading pip, run:*
   ```bash
   python3 -m pip install --upgrade pip
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **View in browser**

   Open http://localhost:5000

## Project Structure

```
python-web-application/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Home page template
└── static/
    ├── styles.css     # Stylesheet
    └── script.js      # JavaScript
```

## Features

- Beginner-friendly Flask web server
- HTML templating with Jinja2
- Static file serving (CSS, JavaScript)
- JSON API endpoint
- Interactive frontend

## Learn More

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python.org](https://www.python.org/)
- [Jinja2 Templates](https://jinja.palletsprojects.com/)
