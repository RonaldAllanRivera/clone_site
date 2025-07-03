````markdown
# 🕸️ Playwright Site Cloner

A powerful script to **clone any modern website**, including **JavaScript-rendered content**, and make it work offline.

This tool uses [Microsoft Playwright](https://playwright.dev/) to simulate a real browser session, download the fully-rendered HTML, static assets (CSS, JS, images), and save everything into a folder you can serve locally.

---

## 🚀 Features

- ✅ Full page rendering via Chromium headless browser
- ✅ Downloads HTML **after JS execution**
- ✅ Captures all CSS, JS, fonts, images (even from CDN)
- ✅ Saves a full-page screenshot
- ✅ Works with dynamic landing pages, funnel sites, affiliate campaigns
- ✅ Easy to view via built-in Python server

---

## 📦 How to Use

### 1. Install dependencies

```bash
pip install -r requirements.txt
playwright install
````

### 2. Clone the target page

Edit the `url` inside `clone_site.py`, then run:

```bash
python clone_site.py
```

This creates:

* `cloned_site/index.html`
* All downloaded resources
* `cloned_site/screenshot.png` (optional)

### 3. Serve it locally

```bash
cd cloned_site
python -m http.server 8000
```

Open: [http://localhost:8000](http://localhost:8000)

---

## 📂 Folder Structure

```
.
├── clone_site.py
├── requirements.txt
├── README.md
├── CHANGELOG.md
└── cloned_site/
    ├── index.html
    ├── screenshot.png
    └── [assets...]
```

---

## 🧠 Notes for Future You

This was built to clone entire dynamic web pages (funnels, LPs, promo sites) for local testing, archiving, or sandbox dev.

You can extend it to:

* Rewrite all relative paths for total offline support
* Clone multi-page sites with a queue
* Handle login-protected pages (via `context.set_cookies()` or `page.fill()`)

---

## ⚠️ Legal Notice

Use this tool only on pages you own or are authorized to clone. Do not use it to violate copyright or terms of service of others.