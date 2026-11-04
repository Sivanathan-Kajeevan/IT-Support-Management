# 🛠️ QuickFix – IT Support Ticket Management System

QuickFix is a web-based IT support ticket management system developed using Python and Django.

The application allows users to report technical problems, track their support tickets, and receive updates from administrators.

## 🚀 Features

### 👤 User Features
- User registration and login
- Create IT support tickets
- Select ticket category and priority
- View submitted tickets
- Track ticket status
- View ticket details

### 🛡️ Administrator Features
- Admin dashboard
- View all support tickets
- Search and filter tickets
- Update ticket status
- Change ticket priority
- Monitor support requests

## 💻 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend programming |
| Django | Web framework |
| SQLite | Database |
| HTML5 | Webpage structure |
| CSS3 | Styling |
| Bootstrap 5 | Responsive design |
| JavaScript | Frontend interactions |

## 📂 Project Structure

```text
QuickFix/
├── quickfix/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── tickets/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── ...
├── templates/
├── static/
│   └── css/
│       └── style.css
├── manage.py
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <YOUR-REPOSITORY-URL>
cd QuickFix
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open the local development server in your browser.

## 🎯 Project Objective

The objective of QuickFix is to simplify IT support management by providing a centralized platform for reporting, monitoring, and resolving technical issues.

## 🔮 Future Improvements

- Email notifications
- Ticket assignment to technicians
- File attachments
- Real-time ticket updates
- Analytics dashboard
- REST API integration

## 📜 License

This project is intended for educational and portfolio purposes.