# Prayer Tracker 🕌

A simple Django-based web application to keep track of daily prayers. This project is designed for learning and basic tracking purposes.

## 🌟 Features

- Add and view your daily prayers.
- Display a list of prayers on a web page.
- Simple and clean interface using Django Templates.

## 🛠️ Tech Stack

- **Backend**: Django 5.2.4
- **Database**: SQLite (default Django setup)
- **Language**: Python 3.13

## 🚀 Getting Started

### 1. Clone the Repository

bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
### 2. Set Up Virtual Environment (Optional but Recommended)
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # For Windows
### 3. Install Requirements
bash
Copy
Edit
pip install django
### 4. Run Migrations
bash
Copy
Edit
python manage.py migrate
### 5. Run the Server
bash
Copy
Edit
python manage.py runserver
Now, visit http://127.0.0.1:8000 in your browser to use the Prayer Tracker app.

### 📁 Project Structure
Copy
Edit
prayertracker/
├── prayers/
│   ├── templates/
│   │   └── tracker.html
│   ├── views.py
│   └── models.py
├── prayertracker/
│   └── settings.py
├── db.sqlite3
└── manage.py
### 📝 License
This project is for educational purposes. Feel free to use and modify it!
