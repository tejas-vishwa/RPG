# Random Password Generator

A clean, modern, and cryptographically secure Random Password Generator application built with Python 3 and Tkinter for desktop, paired with a web application ready for instant deployment to [Vercel](https://vercel.com/).

---

## Features

### 🖥️ Desktop Application (Tkinter)
- Fixed 620x560 desktop window with a modern light theme.
- Header with title and descriptive subtitle: *"Create a strong password in a few simple steps"*.
- Configurable password length (defaults to `12`).
- Labelled **Character Options** frame with 4 independent checkboxes:
  - Uppercase letters (`A-Z`) &mdash; uses `string.ascii_uppercase`
  - Lowercase letters (`a-z`) &mdash; uses `string.ascii_lowercase`
  - Numbers (`0-9`) &mdash; uses `string.digits`
  - Special symbols (`!, @, #, ...`) &mdash; uses `string.punctuation`
- Read-only centered output field formatted in **Consolas** monospace font.
- Three action buttons: **GENERATE PASSWORD**, **COPY PASSWORD**, and **CLEAR**.
- Real-time status bar providing active feedback.

### 🌐 Web Application (Vercel Ready)
- Faithful 1:1 responsive web implementation in `index.html`.
- Uses the standard **Web Crypto API** (`crypto.getRandomValues`) for cryptographically secure pseudo-random number generation.
- Full validation warning dialogs mirroring the desktop experience.
- Optional Python serverless backend API at `/api/generate` (`api/generate.py`) running on Vercel's Python runtime.

---

## Running Locally

### Desktop App (Python 3 Tkinter)
```powershell
py -3 app.py
```

### Run Tests
```powershell
py -3.9 -m unittest test_generator.py
```

### Preview Web Version Locally
You can open `index.html` directly in any web browser, or serve it with Python's built-in HTTP server:
```powershell
py -3 -m http.server 3000
```
Then visit `http://localhost:3000` in your browser.

---

## 🚀 Deploying to Vercel

Since Tkinter is a desktop GUI toolkit requiring a local window manager, the project includes a full web version (`index.html`) and Python serverless function (`api/generate.py`) with `vercel.json` configured for zero-config Vercel deployment.

### Method 1: Deploy via GitHub (Recommended & Easiest)

1. **Create a new repository on GitHub**:
   Go to [github.com/new](https://github.com/new) and create a repository (e.g. `random-password-generator`).

2. **Push your code**:
   ```powershell
   git remote add origin https://github.com/<your-username>/<your-repo-name>.git
   git branch -M main
   git push -u origin main
   ```

3. **Deploy on Vercel**:
   - Go to [vercel.com](https://vercel.com) and log in.
   - Click **"Add New..."** &rarr; **"Project"**.
   - Select your GitHub repository.
   - Leave all default settings as they are and click **"Deploy"**.
   - Your live URL will be ready in seconds!

### Method 2: Deploy via Vercel CLI

If you have Node.js / npm installed:
```powershell
npm install -g vercel
vercel
```
Follow the interactive prompts to link and deploy your project in under a minute.
