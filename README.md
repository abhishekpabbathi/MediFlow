# 🏥 MediFlow – Smart Hospital Management System

## 🚀 Overview

MediFlow is a real-time hospital management system built using Django. It helps manage patients, staff, alerts, and provides intelligent insights using an AI chatbot powered by Groq.

---

## 🧠 Features

* 👨‍⚕️ Staff Management
* 🧑 Patient Management
* 🚨 Alert System
* 📊 Admin Dashboard
* 🤖 AI Chatbot (Groq-powered)
* 🔌 REST API support

---

## 🛠️ Tech Stack

* Backend: Django, Django REST Framework
* AI Integration: Groq API
* Database: SQLite
* Deployment: Whitenoise, Procfile

---

## 📂 Project Structure

```
mediflow/
│
├── patient_mgmt/
├── staff_mgmt/
├── alert_mgmt/
├── chatbot_app/
├── dashboard/
├── manage.py
├── requirements.txt
└── Procfile
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/mediflow.git
cd mediflow
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 🔑 Environment Variables

Create a `.env` file:

```
SECRET_KEY=your_secret_key
DEBUG=True
GROQ_API_KEY=your_api_key
```

---

## 🌐 Future Improvements

* Role-based access (Admin, Doctor, Patient)
* Frontend UI (React / Templates)
* PostgreSQL database
* Deployment on cloud

---

## 👨‍💻 Author

Abhishek Pabbathi
