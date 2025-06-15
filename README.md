# 🔍 Website Crawler with Python (BeautifulSoup + Recursion)

A simple web crawler written in Python that recursively visits internal links of a target website.  
This version specifically targets all pages under **https://www.browse.ai/** and prints them out.

---

## 📌 Features

- ✅ Sends HTTP requests to a target website
- ✅ Parses HTML using `BeautifulSoup`
- ✅ Extracts all internal `<a>` links
- ✅ Recursively visits each internal link only once
- ✅ Ignores fragment identifiers (`#`) to avoid duplication

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`

You can install dependencies with:

```bash
pip install requests beautifulsoup4
