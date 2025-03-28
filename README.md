AuthX - Django Authentication & Authorization System
📌 Overview
AuthX is a Django-based authentication system providing secure user registration, email validation, login, logout, and password reset functionalities. It is structured into one main root project with three apps:

app → User Registration

app1 → User Validation & Login

app2 → Password Reset & Profile Management

It uses Django Rest Framework (DRF), JWT authentication, and django-crispy-forms to enhance security and provide a seamless user experience.

🚀 Features
✅ User Registration with Email Verification

✅ Login & Logout with Secure Authentication

✅ Password Reset via Email Link

✅ Role-Based Access Control (RBAC) for Admins

✅ Session & JWT Authentication Support

✅ Forms Enhanced with django-crispy-forms

📂 Project Structure
authx/
│── project/         # Main Django Project
│── app/           # Handles User Registration
│── app1/          # Handles Login & Validation
│── app2/          # Handles Password Reset & Profile
│── templates/     # HTML Templates (Crispy Forms Used)
│── static/css      # CSS, JS, Images
│── db.sqlite3     # Database (Can switch to PostgreSQL)
│── manage.py      # Django Management Script

🏗 Tech Stack
Backend: Django, Django Rest Framework
Frontend: HTML, CSS, Bootstrap, django-crispy-forms
Database: SQLite 
Authentication: Sessions, JWT, OAuth

🛠 Installation & Setup
1️⃣ Clone & Navigate

git clone https://github.com/yourusername/authx.git
cd authx
2️⃣ Setup Virtual Environment
python -m venv venv
source venv/bin/activate  # Windows: `venv\Scripts\activate`
3️⃣ Install Dependencies

pip install -r requirements.txt
4️⃣ Configure Environment Variables
Create a .env file and add:

env
Copy
Edit
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_password
EMAIL_USE_TLS=True
5️⃣ Run Migrations & Start Server

python manage.py migrate
python manage.py runserver
🔑 API & Web Routes
Feature	Method	Endpoint
Register User	GET/POST	/register/
Validate User	GET/POST	/validate/
Login	GET/POST	/login/
Logout	GET	/logout/
Reset Password	GET/POST	/password-reset/
Update Profile	POST	/profile/update/
Admin Dashboard	GET	/admin-dashboard/
