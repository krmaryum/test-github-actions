# Flask Application - Block by Block Explanation (A to Z)

## Complete Code

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/health')
def health():
    return 'Server is up and running'
```

---

# Overview

This Flask application creates a web server with two routes:

| Route | Purpose |
|---------|---------|
| / | Displays the website home page |
| /health | Returns application health status |

---

# Block 1: Import Statement

```python
from flask import Flask, render_template
```

## Purpose

Imports required components from Flask.

### Flask

```python
Flask
```

Used to create a Flask web application.

### render_template

```python
render_template
```

Used to render HTML files from the templates folder.

---

## Simple Meaning

```text
Flask application aur HTML templates use karne ke liye
required modules import kiye gaye hain.
```

---

# Block 2: Create Flask Application

```python
app = Flask(__name__)
```

## Purpose

Creates a Flask application object.

### app

Main Flask application instance.

### __name__

Python special variable.

Flask uses it to locate:

- Current application
- Templates folder
- Static files

---

## Simple Meaning

```text
Flask application initialize ki gayi hai.
```

---

# Block 3: Home Route

```python
@app.route('/')
```

## Purpose

Creates the home page URL.

Example:

```text
http://127.0.0.1:5000/
```

---

## Route Decorator

```python
@app.route('/')
```

This tells Flask:

```text
When a user visits /
run the following function.
```

---

# Block 4: Home Function

```python
def hello_world():
```

## Purpose

Handles requests for:

```text
/
```

Example:

```text
http://127.0.0.1:5000/
```

---

## Simple Meaning

```text
Home page request handle karne wala function.
```

---

# Block 5: Render HTML Template

```python
return render_template('index.html')
```

## Purpose

Loads and displays:

```text
templates/index.html
```

---

## Folder Structure

```text
project/
│
├── app.py
│
└── templates/
    └── index.html
```

---

## Example

index.html

```html
<h1>Welcome to My Portfolio</h1>
```

Browser Output

```text
Welcome to My Portfolio
```

---

## Simple Meaning

```text
index.html page browser mein display ki ja rahi hai.
```

---

# Block 6: Health Route

```python
@app.route('/health')
```

## Purpose

Creates a health check endpoint.

Example:

```text
http://127.0.0.1:5000/health
```

---

## Why Health Endpoint?

Used by:

- Docker
- Kubernetes
- Load Balancers
- Monitoring Tools
- CI/CD Pipelines
- Cloud Platforms

To verify application status.

---

## Simple Meaning

```text
Application ki health check karne ke liye route.
```

---

# Block 7: Health Function

```python
def health():
```

## Purpose

Handles requests sent to:

```text
/health
```

---

## Simple Meaning

```text
Health endpoint ka response return karne wala function.
```

---

# Block 8: Return Response

```python
return 'Server is up and running'
```

## Purpose

Returns plain text response.

Browser Output:

```text
Server is up and running
```

---

## Why Useful?

Monitoring systems can verify:

```text
Application reachable?
YES

Application responding?
YES
```

---

# Request Flow - Home Page

```text
Browser
    ↓
/
    ↓
hello_world()
    ↓
render_template('index.html')
    ↓
index.html
    ↓
Browser
```

---

# Request Flow - Health Check

```text
Browser
    ↓
/health
    ↓
health()
    ↓
Server is up and running
    ↓
Browser
```

---

# URL Mapping Table

| URL | Function | Response |
|------|----------|----------|
| / | hello_world() | index.html |
| /health | health() | Server is up and running |

---

# Real-World Use Cases

## Home Page

```text
https://myportfolio.com/
```

Displays:

```html
Portfolio Website
```

---

## Health Endpoint

```text
https://myportfolio.com/health
```

Displays:

```text
Server is up and running
```

---

# Flask Concepts Used

| Concept | Purpose |
|----------|----------|
| Flask | Web framework |
| app | Flask application object |
| Route | URL mapping |
| Function | Request handler |
| render_template | Displays HTML |
| Return | Sends response |
| Decorator | Associates URL with function |

---

# Interview Questions

## What is Flask?

A lightweight Python web framework used to build web applications and APIs.

---

## What is a Route?

A route maps a URL to a Python function.

Example:

```python
@app.route('/')
```

---

## What does render_template() do?

Loads and renders an HTML file from the templates directory.

---

## Why use a Health Endpoint?

To verify that the application is running and responding properly.

---

# One-Line Summary

**This Flask application creates a web server with two routes: the home route (/) displays index.html, while the health route (/health) returns a simple status message confirming that the application is running correctly.**
