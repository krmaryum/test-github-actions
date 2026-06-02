# GitHub Pages Custom Domain Setup (GoDaddy + GitHub Pages) – A to Z Notes

## Overview
This guide explains how to connect a custom GoDaddy domain to a GitHub Pages website deployed with GitHub Actions.

---

# Architecture

```text
User Browser
      |
      v
khalidkhan.me
      |
      v
GoDaddy DNS
      |
      v
GitHub Pages
      |
      v
GitHub Repository
(test-github-actions)
```

---

# Prerequisites

- GitHub account
- GitHub repository with GitHub Pages enabled
- GoDaddy domain
- Portfolio website deployed successfully

Example:

```text
Repository:
test-github-actions

Custom Domain:
khalidkhan.me
```

---

# Step 1 – Purchase Domain

Purchase a domain from GoDaddy.

Example:

```text
khalidkhan.me
```

---

# Step 2 – Open DNS Management

GoDaddy:

```text
My Products
→ Domain
→ DNS
```

---

# Step 3 – Remove Existing Website Builder Record

Delete:

```text
Type: A
Name: @
Value: WebsiteBuilder Site
```

This record points to GoDaddy instead of GitHub Pages.

---

# Step 4 – Add GitHub Pages A Records

Add four A records.

| Type | Name | Value |
|------|------|------|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |

TTL: Default

---

# Step 5 – Configure WWW CNAME

Edit or create:

| Type | Name | Value |
|------|------|------|
| CNAME | www | krmaryum.github.io |

---

# Step 6 – Save DNS Records

Save all DNS changes.

DNS propagation may take:

- 5 minutes
- 30 minutes
- Sometimes several hours

---

# Step 7 – Configure GitHub Pages

Repository:

```text
Settings
→ Pages
```

Source:

```text
GitHub Actions
```

---

# Step 8 – Configure Custom Domain

Under Custom Domain:

```text
khalidkhan.me
```

Click:

```text
Save
```

---

# Step 9 – Verify DNS

GitHub should show:

```text
DNS check successful
```

This confirms:

- Domain ownership works
- DNS records are correct
- GitHub Pages can serve the site

---

# Step 10 – SSL / HTTPS

GitHub automatically issues a certificate.

Initially you may see:

```text
Enforce HTTPS unavailable
```

Wait for certificate generation.

---

# Step 11 – Enable HTTPS

Once available:

```text
Enforce HTTPS
```

Enable the checkbox.

---

# Step 12 – Test Website

Open:

```text
https://khalidkhan.me
```

Expected result:

- Site loads
- HTTPS enabled
- Secure connection

---

# DNS Records Summary

| Type | Name | Value |
|------|------|------|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | krmaryum.github.io |

---

# Troubleshooting

## DNS Check Failed

Verify:

- A records are correct
- CNAME points to krmaryum.github.io
- DNS propagation completed

---

## Site Not Loading

Check:

```text
Settings → Pages
```

Ensure:

```text
Custom Domain = khalidkhan.me
```

---

## HTTPS Not Available

Wait longer.

GitHub certificate generation can take:

- Minutes
- Hours
- Occasionally up to 24 hours

---

# Benefits of a Custom Domain

- Professional branding
- Better resume presentation
- Easy sharing
- Recruiter friendly
- Personal ownership

Example:

```text
Portfolio: https://khalidkhan.me
```

---

# Resume Entry

```text
Personal Portfolio Website
• Built and deployed a responsive portfolio website using HTML, CSS, and GitHub Pages.
• Configured custom domain (khalidkhan.me) through GoDaddy DNS.
• Automated deployments using GitHub Actions CI/CD.
• Implemented HTTPS and custom domain routing.
```

---

# Final Result

```text
Domain:
khalidkhan.me

Hosting:
GitHub Pages

Deployment:
GitHub Actions

DNS Provider:
GoDaddy

SSL:
HTTPS Enabled
```
