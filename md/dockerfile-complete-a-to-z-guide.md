# Dockerfile Complete A-to-Z Guide

# Table of Contents

1. What is Dockerfile?
2. Why Do We Need a Dockerfile?
3. Dockerfile Structure
4. FROM Instruction
5. WORKDIR Instruction
6. COPY Instruction
7. RUN Instruction
8. CMD Instruction
9. Complete Dockerfile Explanation
10. Build Process Flow
11. Docker Image vs Container
12. Common Commands
13. Best Practices
14. Interview Questions
15. Summary

---

# 1. What is a Dockerfile?

A Dockerfile is a text file containing instructions that Docker uses to build an image.

Think of it as a recipe.

Example:

```text
Recipe → Cake
Dockerfile → Docker Image
```

---

# 2. Why Do We Need a Dockerfile?

A Dockerfile allows us to:

- Automate image creation
- Install dependencies
- Copy application files
- Configure runtime settings
- Create repeatable builds

Benefits:

- Consistency
- Portability
- Automation
- Easy deployment

---

# 3. Complete Dockerfile

```dockerfile
FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
```

---

# 4. FROM Instruction

```dockerfile
FROM python:3.13-slim
```

## Purpose

Defines the base image.

Docker starts building from this image.

## Components

### python

Official Python image.

### 3.13

Python version.

### slim

Lightweight version of Python image.

---

## Simple Meaning

```text
Start container using Python 3.13 slim image.
```

---

# 5. WORKDIR Instruction

```dockerfile
WORKDIR /app
```

## Purpose

Sets the working directory inside the container.

Equivalent:

```bash
mkdir /app
cd /app
```

---

## Result

```text
Container
└── /app
```

All future commands execute inside:

```text
/app
```

---

# 6. COPY Instruction

```dockerfile
COPY . .
```

## Purpose

Copies files from host machine into container.

### First Dot

```text
Current directory on host
```

### Second Dot

```text
Current directory inside container
```

---

## Example

Host:

```text
project/
├── app.py
├── requirements.txt
└── Dockerfile
```

After COPY:

```text
Container
└── /app
    ├── app.py
    ├── requirements.txt
    └── Dockerfile
```

---

# 7. RUN Instruction

```dockerfile
RUN pip install -r requirements.txt
```

## Purpose

Executes command during image build.

Installs dependencies.

Example requirements.txt:

```text
flask
flake8
```

Docker executes:

```bash
pip install -r requirements.txt
```

---

## Result

Packages become part of the image.

---

# 8. CMD Instruction

```dockerfile
CMD ["python", "app.py"]
```

## Purpose

Defines the default command executed when container starts.

Equivalent:

```bash
python app.py
```

---

## Simple Meaning

```text
Start Flask application when container launches.
```

---

# 9. Complete Build Explanation

```dockerfile
FROM python:3.13-slim
```

Create image from Python base image.

↓

```dockerfile
WORKDIR /app
```

Create and switch to /app.

↓

```dockerfile
COPY . .
```

Copy project files.

↓

```dockerfile
RUN pip install -r requirements.txt
```

Install dependencies.

↓

```dockerfile
CMD ["python", "app.py"]
```

Run application.

---

# 10. Build Process Flow

```text
Dockerfile
     ↓
Docker Build
     ↓
Docker Image
     ↓
Docker Run
     ↓
Container
     ↓
Flask Application
```

---

# 11. Docker Image vs Container

| Image | Container |
|---------|---------|
| Blueprint | Running instance |
| Read-only | Writable |
| Template | Active process |
| Built once | Run many times |

Example:

```text
Image
 ↓
Container 1
Container 2
Container 3
```

---

# 12. Common Docker Commands

## Build Image

```bash
docker build -t flask-app .
```

---

## View Images

```bash
docker images
```

---

## Run Container

```bash
docker run -p 5000:5000 flask-app
```

---

## View Containers

```bash
docker ps
```

---

## Stop Container

```bash
docker stop <container-id>
```

---

# 13. Flask Requirement

Your Flask application should contain:

```python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

Why?

```text
Allow external connections to the container.
```

---

# 14. Interview Questions

## What is a Dockerfile?

A file containing instructions used to build Docker images.

---

## What does FROM do?

Defines the base image.

---

## What does WORKDIR do?

Sets the working directory.

---

## What does COPY do?

Copies files into the image.

---

## What does RUN do?

Executes commands during image build.

---

## What does CMD do?

Defines the default startup command.

---

## Difference between RUN and CMD?

RUN:

```text
Executes during build.
```

CMD:

```text
Executes when container starts.
```

---

# 15. Final Summary

```text
FROM
 ↓
WORKDIR
 ↓
COPY
 ↓
RUN
 ↓
CMD
 ↓
Docker Image
 ↓
Container
 ↓
Application Running
```

---

# One-Line Summary

A Dockerfile is a set of instructions that Docker follows to create an image, install dependencies, copy application files, and define how the application should start inside a container.
