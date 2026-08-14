# 👔 Male Fashion Django E-Commerce

A modern and responsive **men's fashion e-commerce website** built with **Django and Python**. The project provides a complete online shopping experience including product browsing, user accounts, cart, wishlist, orders, reviews, and online payment integration.

## ✨ Features

* 👤 User registration and login
* 🛍️ Browse fashion products
* 🏷️ Products organized by brand and category
* 🔎 Product details and product information
* 🛒 Add to Cart
* ❤️ Wishlist
* 📦 Order management
* ⭐ Product reviews
* 👨‍💼 Admin dashboard
* 🏷️ Brand management
* 📂 Category management
* 📦 Product management
* 💳 Razorpay payment integration
* 👤 User profile management
* 📱 Responsive design

## 🛠️ Technologies Used

### Backend

* Python
* Django

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap

### Database

* SQLite

### Payment Gateway

* Razorpay

## 📁 Project Structure

```text
male-fashion-django-ecommerce/
│
├── fashionapp/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── malefashion/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── static/
│   ├── css/
│   ├── js/
│   ├── img/
│   └── assets/
│
├── template/
│   ├── adminsite/
│   ├── index.html
│   ├── shop.html
│   ├── product-details.html
│   ├── shopping-cart.html
│   ├── checkout.html
│   └── ...
│
├── .gitignore
├── manage.py
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/ravalshubham15/male-fashion-django-ecommerce.git
```

### 2. Open the project folder

```bash
cd male-fashion-django-ecommerce
```

### 3. Create a virtual environment

```bash
py -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install django
```

> If a `requirements.txt` file is added later, use `pip install -r requirements.txt` instead.

### 6. Apply migrations

```bash
py manage.py migrate
```

### 7. Run the development server

```bash
py manage.py runserver
```

Open the website in your browser:

```text
http://127.0.0.1:8000/
```

## 💳 Razorpay Integration

The project includes Razorpay payment integration for online payments.

For security, payment credentials such as API keys should **never be committed to GitHub**. Store sensitive credentials using environment variables or another secure configuration method.

## 📸 Screenshots

Screenshots of the website can be added here to demonstrate:

* 🏠 Home page
* 🛍️ Shop page
* 👕 Product details
* 🛒 Shopping cart
* 💳 Checkout/payment
* 👨‍💼 Admin dashboard

## 🎯 Project Purpose

This project was developed as a **Django-based e-commerce project** to demonstrate practical skills in:

* Web development
* Django framework
* Database management
* User authentication
* E-commerce functionality
* Payment gateway integration
* Frontend development

## 👨‍💻 Developer

**Raval Shubham**

GitHub:
https://github.com/ravalshubham15

## 📄 License

This project is created for educational and project purposes.