---

# 🔍 Text Search API

A simple Django REST API to search for a **keyword** in a given **text** using Docker and PostgreSQL.  
This project demonstrates clean backend architecture with a custom user model, Docker-powered services, and an API-ready interface using Django REST Framework.

---

## 🚀 Features

- 🧩 Django 4.x + PostgreSQL setup using Docker Compose  
- 🔗 Django REST Framework for modular APIs  
- 👤 Extensible custom user model (auth-ready)  
- 🔍 Keyword search API (`/api/search/`)  
- 📦 Containerized setup for easy deployment and scalability

---

## 📂 Project Structure

```
textsearch/
├── Dockerfile
├── docker-compose.yml
├── entrypoint.sh
├── manage.py
├── .env
├── requirements.txt
├── textsearch/           # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── api/                  # Search API app
│   ├── views.py
│   ├── urls.py
│   └── serializers.py
├── users/                # Custom user model
│   ├── models.py
│   ├── admin.py
│   └── ...
```

---

## ⚙️ Environment Configuration (`.env`)

```env
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost 127.0.0.1
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

---

## 🐳 Docker Setup

1. **Build and launch containers**
   ```bash
   docker-compose up --build -d
   ```

2. **Run migrations**
   ```bash
   docker-compose exec web python manage.py makemigrations
   docker-compose exec web python manage.py migrate
   ```

3. **Access API**
   Navigate to: [http://localhost:8000/api/search/](http://localhost:8000/api/search/)

---

## 🔎 Search API Endpoint

**POST** `/api/search/`

### ➡️ Request Body
```json
{
  "text": "Django is a high-level Python web framework.",
  "keyword": "Python"
}
```

### ⬅️ Response
```json
{
  "found": true,
  "message": "Keyword found in text"
}
```

---

## 🧪 Testing

Add unit tests in `api/tests.py` using Django’s testing framework to validate the search logic and endpoint behavior.

---

## 📌 Requirements

- Python 3.11  
- Docker + Docker Compose  
- PostgreSQL (via container)

---

## 🧠 Future Enhancements

- 🔐 Token-based Authentication  
- 🚦 Rate Limiting  
- 📊 Save search history (per user)  
- ☁️ Cloud deployment: Render, Railway, Heroku, etc.

---

## 👨‍💻 Author

**Developed by:** *Anchal Verma*  
Final Year B.Tech Student | Passionate about Backend, DevOps, and Open Source

---

## 📜 License

This project is licensed under the **MIT License**.

---
