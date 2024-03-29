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
    - read, update (including update role), and delete user
    - if 'admin' role choosen, it will be additional form and add to new database admin (still have relational with user) 
- Location
    - Read location
    - Create location
        - Only for superadmin
    - Update location
        - Only for superadmin and admin
        - Admin can only update related location
- Book
    - CRUD Author
        - Delete Only for superadmin
        - Create and Update only for superadmin and admin
    - CRUD Genre
        - Delete Only for superadmin
        - Create and Update only for superadmin and admin
    - CRUD Publisher
        - Delete Only for superadmin
        - Create and Update only for superadmin and admin
    - CRUD Book
        - Delete Only for superadmin
        - Create and Update only for superadmin and admin
- Borrow Book
    - CRUD Borrow
        - Create Borrow request
            - Only if stock book more than 0
        - Read and delete Borrow Request
            - The user can only read and delete requests from him
            - Admin library can only read and delete requests from his authorization
        - Update approval request
            - Admin library can only approve requests from his authorization
        - Read borrowed book and return book
            - The user can only read borrowed book from him
            - Admin library can only read borrowed book from his authorization
        - Update return request
            - Admin library can only approve requests from his authorization

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

