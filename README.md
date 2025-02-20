# E-Commerce Website

## 📌 Project Overview
This is a fully functional e-commerce website built using Django. It allows users to browse products, add items to their cart, place orders, and make secure payments using PayPal. Admins can manage products, and users can register, log in, and update their profiles.

---

## 🚀 Features

### 🔹 User Features
- Browse products and view product details.
- Add products to a shopping cart.
- Register, log in, and log out securely.
- Place and view order history.
- Update profile information.
- Make secure online payments using PayPal.

### 🔹 Admin Features
- Add, edit, and delete products.

### 🔹 Additional Features
- Fully responsive UI (desktop, tablet, mobile).
- Secure authentication and authorization.
- Order management and checkout process.

---

## 🛠️ Technologies Used

### **Frontend:**
- HTML, CSS, JavaScript
- Bootstrap for responsive design

### **Backend:**
- Python & Django
- SQLite
- Django Authentication System
- django-paypal for payments


---

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone <repository_url>
cd ecommerce_project
```

### 2️⃣ Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create a Superuser (Admin Account)
```bash
python manage.py createsuperuser
```

### 7️⃣ Run the Development Server
```bash
python manage.py runserver
```

Open your browser and go to `http://127.0.0.1:8000/`

---

## 📝 To-Do & Future Improvements
- Improve Code Readability 
- Ensure Proper Validations and Error Handling
- Use a .env file to store secrets and sensitive data.
- Write Basic Unit Tests
- Improve UI to better user experience.
- Add another payment option.
- Use docker and GitHub-actions
- Deployment 

---

## ✉️ Contact
For any inquiries, feel free to reach out!

📧 Email: mohamed_salem_ali@outlook.com

