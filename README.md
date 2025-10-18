# 🔗 URL Shortener (Bit.ly Clone)

A simple yet powerful URL shortener service built using **FastAPI + SQLite**.

## 🚀 Features
- Shorten any long URL to a 6-character code.
- Redirect instantly using the shortened link.
- Lightweight and easily deployable (Docker-ready).

## 🧱 Tech Stack
- **Backend:** FastAPI (Python)
- **Database:** SQLite + SQLAlchemy ORM
- **Tools:** Pydantic, Uvicorn

## ▶️ Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/url-shortener.git
cd url-shortener
pip install -r requirements.txt
uvicorn app.main:app --reload
