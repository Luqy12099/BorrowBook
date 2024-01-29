# Django Borrow Book from Library


BookBorrow is a web-based application built using Django and styled with Bootstrap, designed to streamline the process of borrowing and managing books from a library. It serves as a centralized platform for users, admin librarians, and administrators to interact efficiently and effectively.

## Features
- Register
    There is 3 role with default 'user'
    1. superadmin (administrators)
    2. admin (admin librarians)
    3. user
- Login
- Management User
    This feature only for superadmin

## Technologies Used

- Django
- Bootstrap
- crispy-bootstrap4

### Clone, Install, and Run

```bash
# Clone the Repository
git clone https://github.com/Luqy12099/BorrowBook
cd BorrowBook (or your own folder)

# Make new env (Optional)
python -m venv venv_nameYourVenv
venv_nameYourVenv\Scripts\activate

# Install Dependencies
pip install -r pip_req.txt
pip install --upgrade pip
pip install crispy-bootstrap4

# Apply Migrations
cd library
python manage.py makemigrations
python manage.py migrate

# Run the Application
python manage.py runserver

