# Hosting Static Websites from WSL - A to Z Notes

## Overview

Yes, you can host a static website directly from **WSL (Windows Subsystem for Linux)**.

But there are two different meanings of hosting:

```text
1. Local hosting
   Website runs on your own computer.
   You can open it in your browser using localhost.

2. Public hosting
   Website is available on the internet.
   Other people can open it using a public URL.
```

WSL is excellent for local testing and DevOps practice.  
For public hosting, you usually need GitHub Pages, a tunnel, or a cloud server such as AWS EC2.

---

## 1. What is a Static Website?

A static website is a website made of files such as:

```text
index.html
style.css
script.js
images/
```

It does not require a backend server like Flask, Django, Node.js, or PHP.

Examples of static websites:

- Portfolio website
- Resume website
- Documentation website
- Landing page
- Project demo page
- HTML/CSS/JavaScript practice website

---

## 2. What is WSL?

WSL stands for:

```text
Windows Subsystem for Linux
```

It allows you to run Linux inside Windows.

Example:

```text
Windows 11
    ↓
WSL Ubuntu
    ↓
Linux commands
```

In WSL, you can use:

```bash
ls
cd
mkdir
python3
nginx
git
docker
ssh
```

WSL is very useful for DevOps, Linux, Git, Docker, Python, and cloud practice.

---

## 3. Can WSL Host a Website?

Yes.

WSL can host a website locally using:

```text
Python HTTP Server
Nginx
Apache
Docker
Node.js
```

For static websites, the two easiest methods are:

```text
1. Python HTTP Server
2. Nginx
```

---

## 4. Local Hosting vs Public Hosting

| Type | Meaning | Example URL |
|---|---|---|
| Local Hosting | Only your computer can access it | http://localhost:8000 |
| LAN Hosting | Devices on same Wi-Fi/network can access it | http://192.168.1.20:8000 |
| Public Hosting | Anyone on the internet can access it | https://example.com |

WSL is best for:

```text
Local testing
Practice
Development
Learning
```

For public hosting, better options are:

```text
GitHub Pages
Cloudflare Tunnel
ngrok
AWS EC2
DigitalOcean
Azure VM
```

---

## 5. Basic Folder Structure

A simple static website may look like this:

```text
my-website/
├── index.html
├── style.css
├── script.js
└── images/
    └── profile.png
```

The most important file is:

```text
index.html
```

Web servers usually load `index.html` automatically.

---

## 6. Method 1: Host Static Website Using Python HTTP Server

This is the easiest method.

### Step 1: Go to Website Folder

```bash
cd ~/my-website
```

Example:

```bash
cd ~/portfolio
```

Check files:

```bash
ls
```

You should see:

```text
index.html
style.css
script.js
```

---

### Step 2: Start Python Web Server

```bash
python3 -m http.server 8000
```

This starts a simple web server on port `8000`.

You may see output like:

```text
Serving HTTP on 0.0.0.0 port 8000
```

---

### Step 3: Open Website in Windows Browser

Open this in Chrome or Edge:

```text
http://localhost:8000
```

or:

```text
http://127.0.0.1:8000
```

Your website should open.

---

### Step 4: Stop the Server

In WSL terminal, press:

```text
Ctrl + C
```

This stops the Python web server.

---

## 7. Python Server Command Explained

```bash
python3 -m http.server 8000
```

Breakdown:

| Part | Meaning |
|---|---|
| `python3` | Runs Python 3 |
| `-m` | Runs a Python module |
| `http.server` | Built-in Python web server module |
| `8000` | Port number |

Simple meaning:

```text
Use Python to serve the current folder as a website on port 8000.
```

---

## 8. What is a Port?

A port is like a door number for a service.

Examples:

| Port | Common Use |
|---|---|
| 80 | HTTP website |
| 443 | HTTPS website |
| 5000 | Flask app |
| 8000 | Python HTTP server |
| 8080 | Web apps / testing |

When you run:

```bash
python3 -m http.server 8000
```

Your website runs on:

```text
http://localhost:8000
```

---

## 9. Method 2: Host Static Website Using Nginx in WSL

Nginx is a real web server.

It is commonly used in production environments.

---

### Step 1: Install Nginx

```bash
sudo apt update
sudo apt install nginx -y
```

---

### Step 2: Start Nginx

```bash
sudo service nginx start
```

Check status:

```bash
sudo service nginx status
```

---

### Step 3: Open Default Nginx Page

Open in browser:

```text
http://localhost
```

If Nginx is working, you should see the default Nginx welcome page.

---

### Step 4: Copy Website Files to Nginx Web Directory

Nginx default web directory is:

```text
/var/www/html
```

Go to your website folder:

```bash
cd ~/my-website
```

Copy files:

```bash
sudo cp -r * /var/www/html/
```

---

### Step 5: Open Website

Open:

```text
http://localhost
```

Now your static website should appear.

---

## 10. Nginx Commands

### Start Nginx

```bash
sudo service nginx start
```

### Stop Nginx

```bash
sudo service nginx stop
```

### Restart Nginx

```bash
sudo service nginx restart
```

### Check Status

```bash
sudo service nginx status
```

### Test Nginx Configuration

```bash
sudo nginx -t
```

---

## 11. Method 3: Host Static Website Using Docker in WSL

If Docker is installed, you can serve a static website using Nginx container.

Go to your website folder:

```bash
cd ~/my-website
```

Run Nginx container:

```bash
docker run --rm -d   --name static-site   -p 8080:80   -v "$PWD":/usr/share/nginx/html:ro   nginx
```

Open:

```text
http://localhost:8080
```

Stop container:

```bash
docker stop static-site
```

---

## 12. Docker Command Explained

```bash
docker run --rm -d --name static-site -p 8080:80 -v "$PWD":/usr/share/nginx/html:ro nginx
```

| Part | Meaning |
|---|---|
| `docker run` | Start a container |
| `--rm` | Remove container after stopping |
| `-d` | Run in background |
| `--name static-site` | Container name |
| `-p 8080:80` | Host port 8080 maps to container port 80 |
| `-v "$PWD":/usr/share/nginx/html:ro` | Mount current folder into Nginx web folder |
| `nginx` | Image name |

Simple meaning:

```text
Run an Nginx container and serve my current website folder.
```

---

## 13. Accessing WSL Website from Windows

Usually, WSL forwards localhost automatically.

If website runs in WSL on:

```text
localhost:8000
```

You can open in Windows browser:

```text
http://localhost:8000
```

If that does not work, find WSL IP:

```bash
hostname -I
```

Example output:

```text
172.25.123.45
```

Then open:

```text
http://172.25.123.45:8000
```

---

## 14. Accessing WSL Website from Another Device on Same Wi-Fi

This can be tricky because WSL is behind Windows networking.

Basic flow:

```text
Phone / another laptop
        ↓
Windows host IP
        ↓
Port forwarding
        ↓
WSL web server
```

For serious sharing, it is easier to use:

```text
ngrok
cloudflared
GitHub Pages
AWS EC2
```

---

## 15. Can People on the Internet Access My WSL Website?

Not directly by default.

Why?

Because WSL is usually behind:

```text
Internet
    ↓
Home router
    ↓
Windows firewall
    ↓
WSL virtual network
```

So outside users cannot normally access it.

To make it public, you need one of these:

```text
1. GitHub Pages
2. Cloudflare Tunnel
3. ngrok
4. LocalTunnel
5. AWS EC2 / VPS
6. Domain + DNS + public server
```

---

## 16. Public Hosting Option 1: GitHub Pages

Best option for static websites.

Flow:

```text
Static website files
        ↓
GitHub repository
        ↓
GitHub Pages
        ↓
Public URL
```

Example URL:

```text
https://username.github.io/repository-name/
```

Best for:

```text
Portfolio websites
Documentation
HTML/CSS/JS projects
Student projects
```

Benefits:

- Free
- Easy
- Public URL
- HTTPS included
- Good for portfolio

---

## 17. Public Hosting Option 2: Cloudflare Tunnel

Cloudflare Tunnel can expose your local website to the internet.

Flow:

```text
WSL localhost website
        ↓
cloudflared tunnel
        ↓
Public Cloudflare URL
```

Good for:

```text
Temporary demos
Testing webhooks
Sharing work in progress
```

---

## 18. Public Hosting Option 3: ngrok

ngrok creates a temporary public URL for your local website.

Example:

```bash
ngrok http 8000
```

If your website runs on:

```text
http://localhost:8000
```

ngrok gives a public URL like:

```text
https://abc123.ngrok-free.app
```

Good for quick testing.

---

## 19. Public Hosting Option 4: AWS EC2

AWS EC2 is better for real DevOps practice.

Flow:

```text
GitHub repository
        ↓
GitHub Actions
        ↓
EC2 server
        ↓
Nginx / Docker
        ↓
Public IP or domain
```

Good for learning:

- Linux
- SSH
- Nginx
- Docker
- CI/CD
- Security Groups
- DNS
- Deployment

---

## 20. Recommended Learning Path

For your DevOps learning, use this order:

```text
1. WSL + Python HTTP Server
2. WSL + Nginx
3. WSL + Docker Nginx container
4. GitHub Pages
5. AWS EC2 + Nginx
6. AWS EC2 + Docker
7. GitHub Actions deployment
8. Domain + DNS
9. HTTPS with SSL certificate
```

---

## 21. Best Method for Different Needs

| Need | Best Option |
|---|---|
| Quick local test | Python HTTP server |
| Real web server practice | Nginx in WSL |
| Docker practice | Nginx Docker container |
| Free public static hosting | GitHub Pages |
| Temporary public sharing | ngrok or Cloudflare Tunnel |
| Real DevOps deployment | AWS EC2 |
| Production-like hosting | VPS / Cloud + Nginx + SSL |

---

## 22. Full Example: Local Static Hosting with Python

Folder:

```text
portfolio/
├── index.html
├── style.css
└── images/
```

Commands:

```bash
cd ~/portfolio
python3 -m http.server 8000
```

Open:

```text
http://localhost:8000
```

Stop:

```text
Ctrl + C
```

---

## 23. Full Example: Static Hosting with Nginx

Install:

```bash
sudo apt update
sudo apt install nginx -y
```

Start:

```bash
sudo service nginx start
```

Copy website:

```bash
cd ~/portfolio
sudo cp -r * /var/www/html/
```

Open:

```text
http://localhost
```

Restart after changes:

```bash
sudo service nginx restart
```

---

## 24. Full Example: Static Hosting with Docker

```bash
cd ~/portfolio
docker run --rm -d   --name static-site   -p 8080:80   -v "$PWD":/usr/share/nginx/html:ro   nginx
```

Open:

```text
http://localhost:8080
```

Stop:

```bash
docker stop static-site
```

---

## 25. Troubleshooting

### Problem: localhost does not open

Check server is running:

```bash
ps aux | grep python
```

or:

```bash
sudo service nginx status
```

Check port:

```bash
ss -tulnp
```

---

### Problem: Port already in use

Example error:

```text
Address already in use
```

Find process:

```bash
sudo lsof -i :8000
```

Kill process:

```bash
sudo kill -9 <PID>
```

Or use another port:

```bash
python3 -m http.server 8080
```

---

### Problem: Nginx shows default page

Your files may not be copied correctly.

Check:

```bash
ls /var/www/html
```

Make sure `index.html` exists:

```bash
ls /var/www/html/index.html
```

---

### Problem: Permission denied when copying files

Use `sudo`:

```bash
sudo cp -r * /var/www/html/
```

---

### Problem: Website works in WSL but not Windows browser

Try:

```text
http://127.0.0.1:8000
```

Find WSL IP:

```bash
hostname -I
```

Then open:

```text
http://WSL-IP:8000
```

---

### Problem: Other people cannot access my WSL website

This is normal.

WSL local hosting is not public by default.

Use:

```text
GitHub Pages
ngrok
Cloudflare Tunnel
AWS EC2
```

---

## 26. Security Notes

Do not expose your local WSL server publicly without understanding security.

Be careful with:

- Open ports
- Public tunnels
- Sensitive files
- `.env` files
- SSH keys
- API keys
- Private repositories

Never serve a folder that contains secrets.

Bad idea:

```text
Serving your entire home directory
```

Better:

```text
Serve only your website folder
```

Example:

```bash
cd ~/portfolio
python3 -m http.server 8000
```

---

## 27. Difference Between WSL Hosting and GitHub Pages

| WSL Hosting | GitHub Pages |
|---|---|
| Runs on your computer | Runs on GitHub |
| Good for testing | Good for public websites |
| Usually local only | Public URL |
| Stops when terminal/server stops | Always available |
| Needs your computer on | Hosted by GitHub |
| Good for learning Linux | Good for portfolio |

---

## 28. Difference Between WSL Hosting and EC2 Hosting

| WSL | AWS EC2 |
|---|---|
| Local machine | Cloud server |
| Good for practice | Real public server |
| Not public by default | Public IP available |
| Depends on your laptop | Runs 24/7 if active |
| Free locally | May cost money |
| Great for labs | Great for DevOps projects |

---

## 29. Interview Explanation

You can explain it like this:

```text
I can host static websites from WSL using Python's built-in HTTP server, Nginx, or Docker.
For local testing, I can run python3 -m http.server or configure Nginx inside WSL.
However, WSL hosting is mainly local because WSL runs behind Windows networking.
For public hosting, I would use GitHub Pages for static websites or deploy to a cloud server such as AWS EC2.
```

---

## 30. Resume / LinkedIn Sentence

```text
Practiced hosting static websites locally from WSL using Python HTTP Server, Nginx, and Docker-based Nginx containers.
```

Another version:

```text
Configured local static website hosting in WSL and compared deployment options including GitHub Pages, tunnels, and AWS EC2.
```

---

## 31. Quick Command Summary

### Python Server

```bash
cd ~/portfolio
python3 -m http.server 8000
```

Open:

```text
http://localhost:8000
```

---

### Nginx

```bash
sudo apt update
sudo apt install nginx -y
sudo service nginx start
sudo cp -r * /var/www/html/
```

Open:

```text
http://localhost
```

---

### Docker Nginx

```bash
docker run --rm -d   --name static-site   -p 8080:80   -v "$PWD":/usr/share/nginx/html:ro   nginx
```

Open:

```text
http://localhost:8080
```

Stop:

```bash
docker stop static-site
```

---

## 32. Final Summary

You can host static websites from WSL in multiple ways.

For local testing:

```text
WSL + Python HTTP Server
WSL + Nginx
WSL + Docker Nginx
```

For public hosting:

```text
GitHub Pages
ngrok
Cloudflare Tunnel
AWS EC2
VPS
```

Best practical approach:

```text
Local testing in WSL
        ↓
Push code to GitHub
        ↓
Deploy public site with GitHub Pages or EC2
```

---

## 33. One-Line Summary

WSL can host static websites locally using Python, Nginx, or Docker, but for public internet hosting you should use GitHub Pages, a tunnel service, or a cloud server such as AWS EC2.
