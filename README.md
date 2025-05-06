![Screenshot 2025-05-06 163454](https://github.com/user-attachments/assets/55d183f8-18cb-489b-9103-abbf675c34e1)
![Screenshot 2025-05-06 163435](https://github.com/user-attachments/assets/2e8382cf-0882-4304-9ad6-a02ec0146545)


https://github.com/user-attachments/assets/6a3e9489-9091-4e87-a903-7e24e319d5aa

# 📦 Inventory Management System

A Flask-based web application for managing product inventories across multiple locations. This app provides CRUD operations, product movement tracking, and inventory reporting features.

---

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Database**: PostgreSQL

https://github.com/user-attachments/assets/b9735585-aa54-4ebd-a085-203df4a0ed4d


- **Frontend**: HTML, CSS
- **ORM**: SQLAlchemy
- **Other Tools**: Flask-Migrate, Flask-WTF

---

## 📂 Features

- Register and manage **Products**
- Create and assign **Locations**
- Record **Product Movements** (between locations)
- View **Current Inventory** by location
- Generate **Basic Inventory Reports**

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/inventory-management.git
cd inventory-management

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export FLASK_APP=app.py
export FLASK_ENV=development
# On Windows use: set FLASK_APP=app.py

# Initialize the database
flask db init
flask db migrate
flask db upgrade

# Run the application
flask run
