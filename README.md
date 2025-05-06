# 📦 Inventory Management System

A Flask-based web application for managing product inventories across multiple locations. This app provides CRUD operations, product movement tracking, and inventory reporting features.

---

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Database**: PostgreSQL / MySQL
- **Frontend**: HTML, CSS, Bootstrap
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
